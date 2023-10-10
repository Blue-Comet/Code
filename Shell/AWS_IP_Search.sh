#!/bin/bash

## Create by Comet ##

clear

## Use Case 
## ./filename IPaddress
## Example
## ./filename 1.1.1.1

## Backup AWS Credentials

DATE=$(date +%Y-%m-%d)

cp /root/.aws/credentials /root/.aws/credentials_$DATE


WORKSPACE=$(pwd)

#echo -n "Search IP Adress: "
#read IP 

echo "AWS Platform IP Search Scripts"
echo "------------------------------------------------"

## IPINFO FILE RESET ##
rm $WORKSPACE/RESULT
touch $WORKSPACE/RESULT

#echo ""

for LIST in `ls -al $WORKSPACE/KEYS | awk -F " " '{print $9}' | sed '1,3d'`;
do

        #echo "KEY NAME: $LIST"

        cp $WORKSPACE/KEYS/$LIST /root/.aws/credentials
        #aws ec2 describe-network-interfaces --filters Name=addresses.private-ip-address,Values=$1 --query "NetworkInterfaces[*]" | tee -a $WORKSPACE/RESULT

        aws ec2 describe-network-interfaces --filters Name=addresses.private-ip-address,Values=$1 --query "NetworkInterfaces[*]" > $WORKSPACE/RESULT

        SIZE=$(wc -c $WORKSPACE/RESULT | awk -F " " '{print $1}')

        if [ $SIZE -ne 0 ]; then

                clear
                echo "-------------------------------------------------------------------------------------"
                echo "  AWS Account: $LIST   |  $1                                                     "
                echo "+---------------------+-------------------------------------------------------------+"
                echo ""
                cat $WORKSPACE/RESULT
                echo ""
                break
        else
#               echo ""
                echo "|AWS Account: $LIST   |           No Such IP Addess                               |"
        fi
done

cp /root/.aws/credentials_$DATE /root/.aws/credentials
rm -rf cp /root/.aws/credentials_$DATE