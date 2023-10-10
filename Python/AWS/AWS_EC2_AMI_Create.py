import json
import boto3
import time
import re
from collections import ChainMap
from pprint import pprint as pp

client = boto3.client('ec2')

def EC2(): ## BACKUP Tag 기반의 Instance 리스트 추출

    EC2 = client.describe_instances(
        Filters=[
            {
                'Name': 'tag:BACKUP',
                'Values': [
                    'YES',
                ]
            },
        ],
    )
    
    return EC2

def EC2_ID(): ## EC2() 함수에서 추출한 Instance 들에 대한 InstanceID 추출
    
    LIST = EC2()
    
    InstanceId=[]
    
    for data in LIST['Reservations']:
        InstanceId.append(data['Instances'][0]['InstanceId'])
        
    return InstanceId

def EC2_AMI(): ## 추출한 InstanceID 들을 기반으로 AMI 생성
    
    ec2 = boto3.client('ec2')
    ec2_image = boto3.resource('ec2')
    

    ec2_instance_id = EC2_ID() ## LIST ## Instance ID List
    ami_tag_name_list = EC2_NAME() ## NAME ## Image Tag List

    s_datetime = str(time.strftime('%Y-%m-%d', time.localtime(time.time())))

    for idx in (range(len(ec2_instance_id))):
    
        s_ami_name = s_datetime + ' - ' + ami_tag_name_list[idx] + ' - ' + '(' + ec2_instance_id[idx] + ')'
        ami_id_obj=ec2.create_image(InstanceId = ec2_instance_id[idx], NoReboot=True, Name = s_ami_name) ## AMI ID 값
        
        
        ami_id = ami_id_obj.get('ImageId') ## AMI 를 생성할 때 Return 해주는 Image ID 확인 변수
        
    #    print(ami_id_obj.get('ImageId')) ## ami-xxxxxxxxxxxxxx
    #    print(ec2_instance_id[idx])
        
        image = ec2_image.Image(ami_id)
        image.create_tags(Tags=[{'Key': 'BACKUP', 'Value': 'YES'},])  
        
def EC2_NAME():
    LIST = EC2()
    
    NAME_LIST=[]
    
    for data in LIST['Reservations']: ## 데이터 추출용
        NAME_LIST.append(data['Instances'][0]['Tags'])
        
    key_list=[]
    
    for tmp1 in NAME_LIST:
        for tmp2 in tmp1:
            if (tmp2['Key'] == "Name"):
                key_list.append(tmp2['Value'])
    
    return key_list

def lambda_handler(event, context):
    EC2_AMI()
