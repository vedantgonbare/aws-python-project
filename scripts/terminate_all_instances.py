import boto3

# Initialize EC2 resource
ec2 = boto3.resource('ec2')

# Get all instances
instances = ec2.instances.all()  # Returns all instances in your current region

# Collect instance IDs
instance_ids = [instance.id for instance in instances]

if not instance_ids:
    print("No EC2 instances found to terminate.")
else:
    print(f"Terminating instances: {instance_ids}")
    ec2.instances.filter(InstanceIds=instance_ids).terminate()

    # Wait until all instances are terminated
    for instance in instances:
        instance.wait_until_terminated()

    print("✅ All EC2 instances terminated successfully!")
