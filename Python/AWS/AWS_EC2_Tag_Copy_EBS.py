import boto3
import os
import re
from pprint import pprint as pp
os.system('cls')

client = boto3.client('ec2')

ec2_id=[]
ec2_name=[]
ec2_tag_key=[]
ec2_tag_value=[]
ec2_tag_key_value=[]
volume_id=[]

def func_ec2_id():

    response = client.describe_instances()
    
    for id in response['Reservations']:
        ec2_id.append(id['Instances'][0]['InstanceId'])
          
func_ec2_id()

def func_ec2_name():

    for id in ec2_id:
        
        response = client.describe_tags(            
            Filters=[
                {
                    'Name':'resource-id',
                    'Values': [ id ],
                },
            ],
        )

        for name in response['Tags']:
            if name['Key'] == 'Name':
                ec2_name.append(name['Value']) 

func_ec2_name()

def func_ec2_tag():
    
    response = client.describe_instances()

    for ec2_tag in response['Reservations']:
        count = len(ec2_tag['Instances'][0]['Tags'])
        for tag_name in range(0,count):
            ec2_tag_key.append(ec2_tag['Instances'][0]['Tags'][tag_name]['Key'])
            ec2_tag_value.append(ec2_tag['Instances'][0]['Tags'][tag_name]['Value'])

func_ec2_tag()

def func_ebs_id():

    response = client.describe_volumes()

    for id in response['Volumes']:
        volume_id.append(id['Attachments'][0]['VolumeId'])

func_ebs_id()

def func_create_tag():

    count=len(ec2_tag_key)

    for id in volume_id:
        for cnt in range(0,count):

            if ec2_tag_key[cnt] != 'Name':
                print(ec2_tag_key[cnt])

                response = client.create_tags(
                    Resources=[
                        id,
                    ],
                    
                    Tags=[
                        {
                            'Key': ec2_tag_key[cnt],
                            'Value': ec2_tag_value[cnt]
                        },
                    ]
                )

func_create_tag()