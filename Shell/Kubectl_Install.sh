#!/bin/bash

## Create by Comet ##

clear

echo "Kubernetes Download.."
curl -o kubectl https://amazon-eks.s3-us-west-2.amazonaws.com/1.14.6/2019-08-22/bin/linux/amd64/kubectl 
sleep 1
echo ""

echo "Apploy Permission"
chmod +x ./kubectl
sleep 1
echo ""

echo "Binary PATH Copy.."
mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$HOME/bin:$PATH
sleep 1
echo ""

echo "Kubectl Version Test.."
kubectl version --short --client
sleep 1
echo ""
