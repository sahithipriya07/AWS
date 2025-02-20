import boto3

s3 = boto3.client('s3')
bucket_name = 'my-boto3-s3-bucket-sahithi'  # Change this to a globally unique name

response = s3.create_bucket(Bucket=bucket_name)
print(f'Bucket {bucket_name} created successfully!')
