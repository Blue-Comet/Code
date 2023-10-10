#!/bin/bash

## Create by Comet ##

clear

LOGPATH=$(pwd)
rm -rf EKS_INFO.log

echo "###############################################"
echo "          Amazon EKS Start Script          "
echo ""
echo "             Script Example                "
echo "###############################################"
echo ""
echo "Input Cluster Name: EKS-NAME"
echo "Input Cluster Version: 1.14"
echo "Input Cluster Region: us-east-1"
echo "Input Cluster NodeGroup-Name: EKS-NG"
echo "Input Cluster Node-Type: t2.micro"
echo "Input Cluster Node-Count: 2"
echo "Input Cluster Node-Min: 1"
echo "Input Cluster Node-Max: 3"
echo "Input Cluster Private-VPC-Subnet-Id: subnet-xxxxxxxxxxx,subnet-xxxxxxxxxxx"
echo "Input Cluster Public-VPC-Subnet-Id: subnet-xxxxxxxxxxx,subnet-xxxxxxxxxxx"
echo ""
echo -n "Input Cluster Name: "
read NAME
echo -n "Input Cluster Version: "
read VERSION
echo -n "Input Cluster Region: "
read Region
echo -n "Input Cluster NodeGroup-Name: "
read NGName
echo -n "Input Cluster Node-Type: "
read Type
echo -n "Input Cluster Node-Count: "
read Count
echo -n "Input Cluster Node-Min: "
read Min
echo -n "Input Cluster Node-Max: "
read Max
echo -n "Input Cluster Private-VPC-Subnet-Id: "
read -a Private
echo -n "Input Cluster Public-VPC-Subnet-Id: "
read -a Public
echo ""
echo "Cluster Name: $NAME" | tee -a EKS_INFO.log
echo "Cluster Version: $VERSION" | tee -a EKS_INFO.log
echo "Cluster Region: $Region" | tee -a EKS_INFO.log
echo "Cluster NodeGroup-Name: $NGName" | tee -a EKS_INFO.log
echo "Cluster Node-Type: $Type"  | tee -a EKS_INFO.log
echo "CLuster Node-Count: $Count" | tee -a EKS_INFO.log
echo "Cluater Node-Min: $Min" | tee -a EKS_INFO.log
echo "Cluster Node-Max: $Max" | tee -a EKS_INFO.log
echo "Cluster Private-VPC-Subnet-Id: ${Private[0]} ${Private[1]} ${Private[2]} ${Private[3]}" | tee -a EKS_INFO.log
echo "Cluster Public-VPC-Subnet-Id: ${Public[0]} ${Public[1]} ${Public[2]} ${Public[3]}" | tee -a EKS_INFO.log
echo ""
echo -n "Input Value Check (Y/N): "
read VALUE
echo ""

if [ "$VALUE" == Y ]; then

        eksctl create cluster \
                --name $NAME \
                --version $VERSION  \
                --region $Region \
                --nodegroup-name $NGName \
                --node-type $Type \
                --nodes $Count \
                --nodes-min $Min  \
                --nodes-max $Max  \
                --vpc-private-subnets=$Private \
                --vpc-public-subnets=$Public \
                --managed  \
                --asg-access

elif [ "$CLUSTER_VALUE" == N ]; then
        echo "EKS Install Cancel"
fi
