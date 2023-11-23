import s3fs
aws_access_key_id = "" 
aws_secret_access_key= ""
aws_region = "us-east-1"

def connect_to_s3():
    try:
        s3 = s3fs.S3FileSystem(anon=False,
                               key= aws_access_key_id,
                               secret=aws_secret_access_key)
        return s3
    except Exception as e:
        print(e)
# connect_to_s3()


def create_bucket_if_not_exist():
    s3 = s3fs.S3FileSystem(anon=False,
                               key= aws_access_key_id,
                               secret=aws_secret_access_key)
    aws_bucket_name = "redditrawdataterraform"
    try:
        if not s3.exists(aws_bucket_name):
            s3.mkdir(aws_bucket_name)
            print("Bucket created")
        else :
            print("Bucket already exists")
    except Exception as e:
        print(e)
create_bucket_if_not_exist()

# def upload_to_s3(s3: s3fs.S3FileSystem, file_path: str, bucket:str, s3_file_name: str):
#     try:
#         s3.put(file_path, bucket+'/raw/'+ s3_file_name)
#         print('File uploaded to s3')
#     except FileNotFoundError:
        # print('The file was not found')