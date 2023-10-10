import boto3
import os
import re
from pprint import pprint as pp
os.system('cls')

## Must be Have a Tag ('Name' and 'Value')
## Example ('Name' : 'InstanceName')

client = boto3.client('ec2')

ec2id=[]

def desc_ec2_id():

    response = client.describe_instances()
    
    for reservation in response['Reservations']:
        ec2id.append(reservation['Instances'][0]['InstanceId'])

desc_ec2_id()

ec2_name = []

def desc_ec2_name():

    for instanceid in ec2id:
        response = client.describe_tags(
            Filters=[
                {
                    'Name':'resource-id',
                    'Values': [instanceid],
                },
            ],
        )
        
        for data in response['Tags']:
            
            if data['Key'] == 'Name':
                ec2_name.append(data['Value'])

    return ec2_name
                
desc_ec2_name()

name_ec2=[]
name_device=[]
name_volumeid=[]

def create_tag_name():

    response = client.describe_volumes(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': ['*']
            },
         ],
    )
    
    for name in response['Volumes']:
        for data in name['Tags']:
            name_ec2.append(data['Value'])

    for device in response['Volumes']:
        temp_device=device['Attachments'][0]['Device']
        name_device.append(temp_device.replace("/sd","/xvd"))

    for volumeid in response['Volumes']:
        name_volumeid.append(volumeid['Attachments'][0]['VolumeId'])


    count=len(name_ec2)

    for delete in range(0,count):
        response = client.delete_tags(
            Resources=[
                name_volumeid[delete], 
            ],
    
            Tags=[
                {
                    'Key' :'Name',
                    'Value': name_ec2[delete],
                },
            ],
        )

    for create in range(0, count):
        response = client.create_tags(
            Resources=[
            name_volumeid[create],
        ],
    
        Tags=[
            {
                'Key': 'Name',
                'Value': name_ec2[create] + '-' + name_device[create],
            },
        ]
    )
 
create_tag_name()