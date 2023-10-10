import os
import json
import boto3
import datetime
import sys
import pprint
from pprint import pprint as pp

ec = boto3.client('ec2')

debug = False ## Debugging 을 위한 조건 지정
def prt(result, force=False) :
    if ((debug == True) or (force == True)):
        pp(result)

def ec2_tag():
    response = ec.describe_instances(
        Filters=[
            {
                'Name': 'tag:JSCHOI',
                'Values': ['YES']
            }    
        ]
    )

    prt(response)
    return response

def EC2_InstanceID():
    JSTAG_EC2 = ec2_tag()

    InstanceID=[]
    for data in JSTAG_EC2['Reservations']:
        InstanceID.append( data['Instances'][0]['InstanceId'] )

    prt( InstanceID )
    return InstanceID

def Create_AMI(instance):
    create_time = datetime.datetime.now()
    create_fmt = create_time.strftime('%Y-%m-%d')

    AMIid = ec.create_image(
        InstanceId=instance,
        Name="JSCHOI-Lambda - " + instance + " from " + create_fmt,
        Description="Lambda created AMI of Instance " + instance + " from " + create_fmt,
        NoReboot=False
    )

    prt(AMIid)
    return AMIid

def lambda_main():
    os.system('cls')

    InstanceID = EC2_InstanceID()
    prt(InstanceID)

    for instance_id in InstanceID :
        result = Create_AMI(instance_id)
        if( None == result):
            prt("AMI Faile", True)
        else:    
            prt("AMI %s Success" % instance_id, True)

lambda_main()
