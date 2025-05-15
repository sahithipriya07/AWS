import boto3
import json

client = boto3.client('lambda')

# Simulated S3 event payload
event_payload = {
    "Records": [
        {
            "s3": {
                "bucket": {
                    "name": "my-boto-s3-bucket-projectsahithi"
                },
                "object": {
                    "key": "samplefile.txt"
                }
            }
        }
    ]
}

response = client.invoke(
    FunctionName='project-lambda',
    InvocationType='RequestResponse',
    Payload=json.dumps(event_payload)
)

print(response['Payload'].read().decode())
