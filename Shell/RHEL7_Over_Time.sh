#!/bin/bash

## Create by Comet ##

clear

curl http://169.254.169.254/latest/meta-data/instance-type -o EC2_TYPE > /dev/null 2>&1

EC2_TYPE=$(cat EC2_TYPE)
EC2_GENERATION=$(cat EC2_TYPE  | awk -F "." '{print $1}'| grep -o '[0-9]')
DATE=$(date +%Y-%m-%d)
BACKUP_PATH=/tmp/RHEL7_TIMEOUT
TIMEOUT=$(cat /sys/module/nvme_core/parameters/io_timeout)

echo "######## Environment variable ########"
echo "# BACKUP FILE PATH: $BACKUP_PATH "
echo "# EC2 Type : $EC2_TYPE"
echo "# EC2 Family : $EC2_GENERATION th"
echo "######################################"
sleep 3

if [ ! -d /tmp/RHEL7_TIMEOUT ]; then
        mkdir $BACKUP_PATH
fi

if [ $EC2_GENERATION -ge 5  ]; then

        echo ""
        echo "EC2 Family is 5 Over Generaetion"
        echo "######################################"

        # Kernel Timeout Parameter 30s Check
        echo ""
        echo "IO_TIMEOUT : $TIMEOUT"
        echo ""

        # GRUB & IO_TIMEOUT Backup
        sudo cp /etc/default/grub $BACKUP_PATH/grub_$DATE
        sudo cp /sys/module/nvme_core/parameters/io_timeout $BACKUP_PATH/io_timeout_$DATE

        # GRUB file Modify and Add nvme_core.io_timeout=4294967295 Parameter
        echo "## Befor Grub File Parameter"
        cat /etc/default/grub | grep GRUB_CMDLINE_LINUX
        sudo sed -i 's/crashkernel=auto/crashkernel=auto nvme_core.io_timeout=4294967295/g' /etc/default/grub

        echo ""
        echo "## After Grub File Parameter"
        cat /etc/default/grub | grep GRUB_CMDLINE_LINUX
        echo ""

        # GRUB.CFG Update
        echo "## GRUB.CFG Update"
        sudo grub2-mkconfig -o /boot/grub2/grub.cfg
        sleep 3
        echo ""

        # System Reboot
        echo -n "Are you Reboot System NOW? (Y/N): "
        read REBOOT

        if [ $REBOOT == "Y" ]; then
                echo "Reboot Now"
                sleep 3
                reboot
        else
                echo "No Reboot, Please Reboot later"
        fi

else
        echo ""
        echo "EC2 Family is 5 Under Generation"
        echo "################################"
        echo "No Try WORK"
        echo ""
fi
