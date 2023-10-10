import boto3
from pprint import pprint as pp

import os
os.system('cls')

bucket_name=[] ## Bucket Name 추가
bucket_obj = [] ## Bucket Key 추가
bucket_obj_sum = []

def func_bucket_name():

    client = boto3.client('s3')
    response = client.list_buckets()
    
    for list in response['Buckets']: ## Buckets 전체 값이 있는데 한번씩 뽑는거 
        bucket_name.append(list['Name'])

func_bucket_name()

def func_object_key():
    
    for bucket_name_list in bucket_name:
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(bucket_name_list)
    
        total_sum = 0

        for obj in bucket.objects.all():
            s3 = boto3.client('s3')
            bucket_obj.append(obj.key)

            response = s3.head_object(Bucket=bucket_name_list, Key=obj.key)            
            size = response['ContentLength']
            total_sum += size

        total_sum_kb = total_sum/1024
        total_sum_mb = total_sum/1024/1024

        print("----")
        print("Bucket Name : %s , Size: %s KB" % (bucket_name_list, round(total_sum_kb,2)))
        print("Bucket Name : %s , Size: %s MB" % (bucket_name_list, round(total_sum_mb,2)))
        print(" ")

func_object_key()