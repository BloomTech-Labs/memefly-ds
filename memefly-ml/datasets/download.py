import boto3
import json
from decouple import config
import os
import requests
import logging
import time


def download_base_memes_from_s3_bucket(pic_dir_path):
    
    if not os.path.exists(pic_dir_path):
        os.makedirs(pic_dir_path, exist_ok=True)
    
    bucket_name = 'memefly-datalake'
    s3_folder = 'base-meme-images'   
    
    s3 = boto3.client(
        's3',
        aws_access_key_id=config('AWS_ACCESS_KEY'),
        aws_secret_access_key=config('AWS_SECRET_ACCESS_KEY')
    )
    
    objs = s3.list_objects(Bucket=bucket_name)
    print(objs)
    for obj in objs['Contents']:
        print(obj)
        if obj['Key'].endswith('.jpg'):
            #print(obj['Key'])
            s3_file_path = obj['Key']
            #print(s3_file_path)
            # s3_folder = s3_file_path.split('/')[0]
            # s3_pic_name = s3_file_path.split('/')[1]
            # pic_download_loc = os.path.join(pic_dir_path, s3_pic_name)
            # s3.download_file(bucket_name, s3_file_path, pic_download_loc)
            # print(f'Downloaded to: {pic_download_loc}')


download_base_memes_from_s3_bucket('../datasets/memefly_0.1')
