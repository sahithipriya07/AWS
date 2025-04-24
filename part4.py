import boto3

s3 = boto3.client('s3')
bucket_name = 's3bucketsahithi'  # Replace with your actual bucket name

response = s3.list_objects_v2(Bucket=bucket_name)
files = response.get('Contents', [])

if files:
    print(f"Files in bucket '{bucket_name}':")
    for file in files:
        print(f"- {file['Key']}")
else:
    print(f"No files found in bucket '{bucket_name}'.")