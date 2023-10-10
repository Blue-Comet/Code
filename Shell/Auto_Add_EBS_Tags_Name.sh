#!/bin/bash

## Create by Comet ##

clear

curl http://169.254.169.254/latest/meta-data/instance-id > /dev/null 2>&1 > EC2_ID
EC2ID=$(cat EC2_ID)

aws ec2 describe-instances --instance-ids $EC2ID --query "Reservations[*].Instances[*].{Name:Tags[?Key=='Name']|[0].Value}" --output=text > EC2_NAME
EC2NAME=$(cat EC2_NAME)

aws ec2 describe-volumes --filters Name=attachment.instance-id,Values=$EC2ID --query "Volumes[*].{ID:VolumeId,InstanceId:Attachments[0].Device}" --output=text > ID_DEVICE

sed -i 's/\t/_/g' ID_DEVICE

FILE=$(cat ID_DEVICE)

echo "EC2 Instance ID: $EC2ID"
echo "EC2 Name: $EC2NAME"
echo "-----------------------------------------"

for DATA in $FILE; do
        VOLUMEID=$(echo $DATA| awk -F "_" '{print $1}')
        DEVICENAME=$(echo $DATA| awk -F "_" '{print $2}')

        aws ec2 create-tags --resources $VOLUMEID --tags "Key=Name,Value=$EC2NAME-$DEVICENAME"


done


for DATA2 in $FILE; do

        aws ec2 describe-tags --filters "Name=resource-id,Values=$VOLUMEID" --output=table

done
