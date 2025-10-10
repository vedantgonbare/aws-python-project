import boto3

# Enter your bucket name
bucket_name = "vedant-test-bucket-12345"  # must be globally unique

# Create S3 client
s3 = boto3.client('s3')

# Create the bucket
try:
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'}
    )
    print(f"Bucket '{bucket_name}' created successfully!")
except Exception as e:
    print("Error:", e)
