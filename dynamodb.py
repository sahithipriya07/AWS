import boto3

# Create a DynamoDB client
dynamodb = boto3.client('dynamodb')
table_name = 'MyDynamodb'  # Change to your preferred table name

# Create the table
response = dynamodb.create_table(
    TableName=table_name,
    KeySchema=[
        {
            'AttributeName': 'ID',
            'KeyType': 'HASH'  # Partition key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'ID',
            'AttributeType': 'S'  # 'S' for string
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)
print(f"Table '{table_name}' creation started. Status: {response['TableDescription']['TableStatus']}")