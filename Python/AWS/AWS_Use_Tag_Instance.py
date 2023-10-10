import json
import boto3
import os
from pprint import pprint as pp

os.system('cls')
client = boto3.client('ec2')

def ec2_tag():
        response = client.describe_instances(
            Filters=[
                {
                    'Name': 'tag:JSTAG',
                    'Values': ['YES']
                }    
            ]
        )

        return response
        
def lambda_main(event, context):
    
    JSTAG_EC2=ec2_tag()
    #pp(type(TAG_EC2_JSTAG))
    #pp(TAG_EC2_JSTAG["Reservations"])
    JSTAG_EC2_Reservations=(JSTAG_EC2["Reservations"]) 
    #pp(TAG_EC2_JSTAG_Reservations[0])
    JSTAG_EC2_Reservations_LIST=JSTAG_EC2_Reservations[0]
    #pp(TAG_EC2_JSTAG_Reservations_LIST["Instances"])
    JSTAG_EC2_Reservations_LIST_DICT=JSTAG_EC2_Reservations_LIST["Instances"]
    #pp(TAG_EC2_JSTAG_Reservations_LIST_DICT[0])
    JSTAG_EC2_Reservations_LIST_DICT_DICT=JSTAG_EC2_Reservations_LIST_DICT[0]
    #pp(JSTAG_EC2_Reservations_LIST_DICT_DICT["InstanceId"])

    DATA_RESERVATIONS_LIST=[]

    for DATA in JSTAG_EC2["Reservations"]:
        #pp(DATA)
        for DATA_RESERVATIONS_INSTANCES in DATA["Instances"]:
            
            #pp(DATA_RESERVATIONS_INSTANCES.keys())
            InstanceID=DATA_RESERVATIONS_INSTANCES.get('InstanceId')
            ImageID=DATA_RESERVATIONS_INSTANCES.get('ImageId')
            KeyName=DATA_RESERVATIONS_INSTANCES.get('KeyName')
            PrivateIpAadress=DATA_RESERVATIONS_INSTANCES.get('PrivateIpAddress')
            VpcId=DATA_RESERVATIONS_INSTANCES.get('VpcId')
            SubnetId=DATA_RESERVATIONS_INSTANCES.get('SubnetId')
            InstanceType=DATA_RESERVATIONS_INSTANCES.get('InstanceType')

            print("JSTAG Usage Instacne Information : ")
            print("-----------------------------------------------------")
            print("InstaceID = %s " % InstanceID)
            print("KeyName = %s " % KeyName)
            print("PrivateIpAddress = %s " % PrivateIpAadress)
            print("VpcId = %s " % VpcId)
            print("SubnetId = %s " % SubnetId)
            print("InstaceType = %s " % InstanceType)
