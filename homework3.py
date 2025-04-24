import json
import logging

def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        size = record['s3']['object'].get('size', 'Unknown')

        logging.info(f"New file uploaded to {bucket}: {key} (Size: {size})")

    return {
        'statusCode': 200,
        'body': json.dumps('Lambda execution successful')
    }
