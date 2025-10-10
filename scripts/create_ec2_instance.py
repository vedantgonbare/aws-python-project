import boto3

# EC2 resource
ec2 = boto3.resource('ec2', region_name='ap-south-1')

# Find the latest Amazon Linux 2 AMI automatically
client = boto3.client('ec2', region_name='ap-south-1')
response = client.describe_images(
    Owners=['amazon'],
    Filters=[
        {'Name': 'name', 'Values': ['amzn2-ami-hvm-*-x86_64-gp2']},
        {'Name': 'state', 'Values': ['available']}
    ]
)

# Sort by creation date descending to get the latest AMI
images = sorted(response['Images'], key=lambda x: x['CreationDate'], reverse=True)
latest_ami_id = images[0]['ImageId']
print("Using latest AMI ID:", latest_ami_id)

# Launch EC2 instance
instances = ec2.create_instances(
    ImageId=latest_ami_id,
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='vedant-key'  # Replace with your key pair name
)

print("EC2 Instance Created! ID:", instances[0].id)
