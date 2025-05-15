import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')
instance_id = 'i-02409a1a1923eb8a7'

response = ec2.describe_instances(InstanceIds=[instance_id])

instance = response['Reservations'][0]['Instances'][0]
metadata = {
    'Instance ID': instance['InstanceId'],
    'AMI ID': instance['ImageId'],
    'Instance Type': instance['InstanceType'],
    'Private IP': instance.get('PrivateIpAddress', 'N/A'),
    'Public IP': instance.get('PublicIpAddress', 'N/A'),
    'Availability Zone': instance['Placement']['AvailabilityZone'],
    'State': instance['State']['Name'],
    'Security Groups': [sg['GroupName'] for sg in instance['SecurityGroups']]
}

for key, value in metadata.items():
    print(f'{key}: {value}')