import boto3
import datetime

# Initialize clients
ec2 = boto3.resource('ec2', region_name='ap-south-1')
s3 = boto3.client('s3', region_name='ap-south-1')

# -----------------------------
# Step 1: Create S3 bucket
# -----------------------------
bucket_name = f"vedant-demo-bucket-{int(datetime.datetime.now().timestamp())}"
s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'}
)
print(f"S3 Bucket Created: {bucket_name}")

# Upload a sample file to the S3 bucket
file_name = "test.txt"
s3.upload_file(file_name, bucket_name, file_name)
print(f"File '{file_name}' uploaded successfully to bucket '{bucket_name}'")

# Add tags to the S3 bucket
s3.put_bucket_tagging(
    Bucket=bucket_name,
    Tagging={
        'TagSet': [
            {'Key': 'Project', 'Value': 'AWS Automation'},
            {'Key': 'Environment', 'Value': 'Development'}
        ]
    }
)
print(f"Tags added to S3 bucket: {bucket_name}")

# -----------------------------
# Step 2: Launch EC2 Instance
# -----------------------------
# Fetch the latest Amazon Linux 2 AMI ID dynamically
ec2_client = boto3.client('ec2', region_name='ap-south-1')
response = ec2_client.describe_images(
    Owners=['amazon'],
    Filters=[{'Name': 'name', 'Values': ['al2023-ami-*-kernel-6.1-x86_64']}]
)
images = sorted(response['Images'], key=lambda x: x['CreationDate'], reverse=True)
latest_ami_id = images[0]['ImageId']
print(f"Using latest AMI ID: {latest_ami_id}")

# Create EC2 instance
instances = ec2.create_instances(
    ImageId=latest_ami_id,
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1,
    KeyName='vedant_key',  # Use your exact key pair name
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {'Key': 'Project', 'Value': 'AWS Automation'},
                {'Key': 'Environment', 'Value': 'Development'}
            ]
        }
    ]
)

instance = instances[0]
instance.wait_until_running()
instance.reload()

print(f"EC2 Instance Created! ID: {instance.id}")
print(f"Public IP Address: {instance.public_ip_address}")
