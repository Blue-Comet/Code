import json
import boto3

client = boto3.client('ec2')

def lambda_handler(event, context):
    
    ec2_tag = client.describe_instances(
        
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': [
                    'string',
                ]
            },
        ],
    )
    
    print(ec2_tag)
