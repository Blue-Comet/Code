import json
import boto3
from pprint import pprint as pp
#import pandas as pd

client = boto3.client('ec2')
ec2 = boto3.client('ec2')

#def lambda_handler(event, context):

def lambda_main(event, context):
    Running = ec2_list_running()
    
    #print("======keys=========")
    #print(Running.keys())
    #print(Running.get("InstanceStatuses"))
    data=(Running.get("InstanceStatuses"))
    
    #data.get(0)
    for list_data in data:
        #print(list_data)
        #print(list_data.get("InstanceState"))
        temp_data = list_data.get("InstanceState")
        print(temp_data.get("Name"))
        
    
    #print(type(data))
    #print("===============")
    #print(Running.get("ResponseMetadata"))
    

"""
for i in param1:
        param2 = temp1.get("HTTPHeaders")
"""
    
    #print(Running.keys())
    #print(Running.values())
    #pp(Running)
    #Running_list=list(Running['InstanceStatuses'])
    #pp(Running_list)
    
def ec2_list_running():
    respone = client.describe_instance_status(

        Filters=[
            {
                'Name': 'instance-state-name' ,
                'Values' : [
                    'running',
                    ]
            }
        ]
    )
    
    return respone       
             
"""
    ec2_tag = client.describe_instances(
        
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': [
                    'junseok-win-2016',
                ]
            },
        ],
    )
"""
