import json
import boto3
import time
from pprint import pprint as pp

client = boto3.client('ec2')

def EC2():
    EC2 = client.describe_instances(
        Filters=[
            {
                'Name': 'tag:Scheduler',
                'Values': [
                    'Weekday',
                ]
            },
        ],
    )
    
    return EC2

def EC2_ID():
    LIST = EC2()
    
    InstanceID=[]
    for data in LIST['Reservations']:
        InstanceID.append( data['Instances'][0]['InstanceId'] )
    
    return InstanceID
    
def EC2_STOP():
    ec2 = boto3.client('ec2')
    today = time.strftime('%c', time.localtime(time.time()))
    LIST=EC2_ID()

    ec2.start_instances(InstanceIds=LIST)
    print('START TIME: ', time.strftime('%c', time.localtime(time.time())))
    print('EC2 START : ', str(LIST))

def lambda_handler(event, context):
    EC2_STOP()
