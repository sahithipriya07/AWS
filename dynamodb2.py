import boto3

# Initialize DynamoDB Client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('MyDynamodb')

# Insert Data
table.put_item(Item={
    'ID': 'A1',
    'Name': 'Amy',
})

# Retrieve Data
response = table.get_item(Key={'ID': 'A1'})
print(response['Item'])