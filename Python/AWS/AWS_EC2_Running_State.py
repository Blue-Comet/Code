import json
import boto3

client = boto3.client('ec2')

def lambda_handler(event, context):
    
    ec2_running = client.describe_instance_status(

        Filters=[
            {
                'Name': 'instance-state-name' ,
                'Values' : [
                    'running',
                    ]
            }
        ]
    )
    
    print(ec2_running)
