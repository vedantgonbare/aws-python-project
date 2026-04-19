import boto3
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize clients
ec2 = boto3.resource('ec2')
s3 = boto3.resource('s3')

INSTANCE_ID = os.getenv('INSTANCE_ID')
BUCKET_NAME = os.getenv('BUCKET_NAME')

# 1️⃣ Terminate EC2 Instance
try:
    instance = ec2.Instance(INSTANCE_ID)
    instance.terminate()
    print(f"Terminating EC2 instance: {INSTANCE_ID} ...")
    instance.wait_until_terminated()
    print(f"✅ EC2 instance {INSTANCE_ID} terminated successfully!")
except Exception as e:
    print(f"⚠️ Error terminating EC2 instance: {e}")

# 2️⃣ Delete all files from S3 bucket
try:
    bucket = s3.Bucket(BUCKET_NAME)
    bucket.objects.all().delete()
    print(f"🗑️ All objects deleted from S3 bucket: {BUCKET_NAME}")
except Exception as e:
    print(f"⚠️ Error deleting objects from S3: {e}")

# 3️⃣ Delete S3 bucket
try:
    bucket.delete()
    print(f"✅ S3 bucket '{BUCKET_NAME}' deleted successfully!")
except Exception as e:
    print(f"⚠️ Error deleting S3 bucket: {e}")
