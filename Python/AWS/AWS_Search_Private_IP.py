import boto3
from pprint import pprint as pp
import os
os.system('cls')

client = boto3.client('ec2')

ipaddress=input("Input Find Private IP Addres: ")
print(ipaddress)

response_pip = client.describe_addresses(
        Filters=[
        {
            'Name' : 'private-ip-address',
            'Values' : [
                ipaddress,
            ],
            'Name' : 'domain',
            'Values' : [
                'vpc',
            ],
        },
    ],
)

eni_id=[]

eni_id.append(response_pip['Addresses'][1]['NetworkInterfaceId'])

response_eid = client.describe_network_interfaces(
    NetworkInterfaceIds=eni_id
   
)

print("---------------------------------------------------------------------------------")
pp(response_eid['NetworkInterfaces'][0]['Groups'])
