#!/bin/bash

## Create by Comet ##

clear

if [ -d logs ]; then
	echo""
	echo "Already exit logs Directory"
	echo "" > logs/eks_install.log
else
	mkdir logs

fi

echo ""
echo -n "AWS Command Line Interface Apply on Server (Y/N): " 
read VALUE

if [ "$VALUE" == Y ]; then
	echo "" | tee -a logs/eks_install.log	
	echo [ "Python2-pip Install.. ]" | tee -a logs/eks_install.log
	sudo yum install python2-pip | tee -a logs/eks_install.log
	sleep 1

        echo "" | tee -a logs/eks_install.log
	echo "[ AWSCLI Install from PIP.. ]" | tee -a logs/eks_install.log
	sudo pip install awscli --upgrade --user | tee -a logs/eks_install.log
	sleep 1

	echo "" | tee -a logs/eks_install.log
	echo "[ EKSCTL Download.. ]" | tee -a logs/eks_install.log
	curl --silent --location "https://github.com/weaveworks/eksctl/releases/download/latest_release/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp | tee -a logs/eks_install.log
	sleep 1

        echo "" | tee -a logs/eks_install.log
	sudo mv /tmp/eksctl /usr/local/bin 
	sleep 1
	
        echo "" | tee -a logs/eks_install.log
	echo "[ EKSCTL Version Check.. ]" | tee -a logs/eks_install.log
	eksctl version | tee -a logs/eks_install.log

else
	echo ""
	echo "FIrst Apply AWS Command Line Interface on Server!!" | tee -a logs/eks_install.log
	echo ""
fi
