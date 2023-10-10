import json
import boto3 
import datetime
from pprint import pprint as pp

client = boto3.client('ec2')
    
def get_image():

    response = client.describe_images(
        Filters=[
            {
                'Name': 'tag:AMI',
                'Values': [
                    'YES',
                ]
            },
        ],
    )
    
    return response

def process_func():
    
    img_data=get_image()
    
    ami_arr = []
    id_arr = []
    
    today = datetime.datetime.now()
    
    data = img_data['Images']
    
    for idx in range(len(data)):
        ami_arr.append([])
        ami_arr[idx].append( data[idx]['ImageId'])
        ami_arr[idx].append( data[idx]['Name'])
        ami_arr[idx].append( data[idx]['CreationDate'])
        
        date_time = data[idx]['CreationDate']
        date_time = date_time.replace("T", " ")
        date_time = date_time.replace("Z", "")
        date_time_obj = datetime.datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S.%f')

        days = (today - date_time_obj).days

        if(days > 30):
            id_arr.append(data[idx]['ImageId'])
        
    return id_arr
    
    
def remove_img():
    
    remove_img_list=process_func()
    
    for ami in remove_img_list:)
        client.deregister_image(ImageId=ami)

def lambda_handler(event, context):
    remove_img()
