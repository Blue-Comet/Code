import json
import boto3 
import datetime
from pprint import pprint as pp

client = boto3.client('ec2')
    
def get_image():

    response = client.describe_images(
        Filters=[
            {
                'Name': 'tag:BACKUP',
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

        if(days < -7): ## Delete Days Configurt Parameter
            id_arr.append(data[idx]['ImageId'])
        
    return id_arr
    
def snapshot():
    
    response = client.describe_snapshots(
            OwnerIds=[
                '@YOUR_AWS_ACCOUNTNUNBER' # Int Type
        ],
    )
    
    return response

def remove_img():
    
    snapshot_list=snapshot()
    remove_img_list=process_func()
    
    final_ami_id=[]
    final_snapshot_id=[]

    snapshot_Snapshots=snapshot_list['Snapshots']
    
    for snapshot_id in snapshot_Snapshots:
        snapshot_ami_id=snapshot_id['Description'].split(' ')[4]
        snapshot_snapshotId=snapshot_id['SnapshotId']
        
        for delete_ami_id in remove_img_list:
            if snapshot_ami_id == delete_ami_id:
                
                final_ami_id.append(snapshot_ami_id)
                final_snapshot_id.append(snapshot_snapshotId)

    for final_delete_ami_id in set(final_ami_id):
        print("Delete AMI ID: %s " % final_delete_ami_id)
        client.deregister_image(ImageId=final_delete_ami_id)

    print("==========================================")
        
    for final_delete_snapshot in final_snapshot_id:
        print("Delete Snapshot ID : %s" % final_delete_snapshot)
        client.delete_snapshot(SnapshotId=final_delete_snapshot)
    

def lambda_handler(event, context):
    remove_img()
