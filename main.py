import os
from src.extract import extract_transactional_data
from src.transform import remove_duplicates
from src.load_data_to_s3 import connect_to_s3,df_to_s3
from dotenv import load_dotenv
load_dotenv()

password= os.getenv('password')
user_name=os.getenv('user')
port=os.getenv('port')
host=os.getenv('host')
dbname=os.getenv('dbname')
aws_access_key_id=os.getenv('aws_access_key_id')
aws_secret_access_key=os.getenv('aws_secret_access_key')
aws_s3_bucket=os.getenv('aws_s3_bucket')

online_trans_transformed=extract_transactional_data(dbname,host,port,user_name,password)

online_trans_transformed_dedub=remove_duplicates(online_trans_transformed)


key='transformations_final/lg_online_trans_transformed.pkl'
df_to_s3(online_trans_transformed_dedub, key, aws_s3_bucket, aws_access_key_id, aws_secret_access_key)
