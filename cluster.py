import configparser
import os
config = configparser.ConfigParser()
config.read_file(open('Cluster/cluster.config'))



SECRET = config.get('api_keys', 'reddit_secret_key')
CLIENT_ID = config.get('api_keys', 'reddit_client_id')
print(SECRET)
print(CLIENT_ID)


# POSTGRESQL
# DATABASE_HOST =  parser.get('database', 'database_host')
# DATABASE_NAME =  parser.get('database', 'database_name')
# DATABASE_PORT =  parser.get('database', 'database_port')
# DATABASE_USER =  parser.get('database', 'database_username')
# DATABASE_PASSWORD =  parser.get('database', 'database_password')

#AWS
AWS_ACCESS_KEY_ID = config.get('aws', 'aws_access_key_id')
AWS_ACCESS_KEY = config.get('aws', 'aws_secret_access_key')
AWS_REGION = config.get('aws', 'aws_region')
AWS_BUCKET_NAME = config.get('aws', 'aws_bucket_name')
print(AWS_BUCKET_NAME)


# INPUT_PATH = parser.get('file_paths', 'input_path')
# OUTPUT_PATH = parser.get('file_paths', 'output_path')

POST_FIELDS = (
    'id',
    'title',
    'score',
    'num_comments',
    'author',
    'created_utc',
    'url',
    'over_18',
    'edited',
    'spoiler',
    'stickied'
)