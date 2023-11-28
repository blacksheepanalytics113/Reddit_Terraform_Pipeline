import s3fs
import botocore
from boto3.s3.transfer import S3Transfer
import boto3
import datetime
from spark import spark_adm

aws_access_key_id = "AKIAXQ3PNDPNLHV3R2ON" 
aws_secret_access_key = "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"
aws_region = "eu-north-1"
aws_bucket_name = "redditrawdataterraform"
file_path = "C:/Users/user/Desktop/Data Engineering Projects(Personal)/AWS_Reddit_Terraform/Csv_Load/Transform_Data/new_data.csv"
s3_file_name = "s3://redditrawdataterraform/Transformed_Data/"
file_name = "Reddit_New.csv"
def connect_to_s3():
    """
    Post All Data saved to s3 Bucket
    """
    try:
        s3 = s3fs.S3FileSystem(anon=False,
                               key= aws_access_key_id,
                               secret=aws_secret_access_key,
                               client_kwargs={
                                'region_name': 'eu-north-1'
    })
        # return s3
        if not s3.exists(aws_bucket_name):
                s3.mkdir(aws_bucket_name)
                print("Bucket created")
        else :
            print("Bucket already exists")
        s3_objects = s3.ls(aws_bucket_name)
        print(s3_objects)
        current_time= datetime.datetime.now()
        Bucket_file_name =   str(current_time)
        Bucket_file_name = Bucket_file_name + file_name 
        print(Bucket_file_name)
        if s3.upload(file_path,f"{aws_bucket_name}/Transformed_Data/"+ file_name):
        # print(upload_data)
            print(f"File uploaded successfully to s3://{aws_bucket_name}/Transformed_Data/" + Bucket_file_name)
        else:
            # FileNotFoundError:
            print('The file was not found')   
        response = s3.put_file(file_path,f'{aws_bucket_name}/{s3_file_name}')
        if response == None:
            print(f"File Uploaded Nothing")
        else:
            print(f"print found success!")
        
        
    except Exception as e:
        print(e)
connect_to_s3()

