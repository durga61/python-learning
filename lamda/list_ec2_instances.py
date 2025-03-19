import boto3

# Create EC2 client
ec2_client = boto3.client("ec2")

# Fetch running instances
response = ec2_client.describe_instances(
    Filters=[{"Name": "instance-state-name", "Values": ["running"]}]
    Filters=[{ "Values": ["running"]}]
)

print(response)

# Extract instance details
# running_instances = []
# for reservation in response["Reservations"]:
#     for instance in reservation["Instances"]:
#         instance_id = instance["InstanceId"]
#         instance_type = instance["InstanceType"]
#         public_ip = instance.get("PublicIpAddress", "N/A")
#         private_ip = instance.get("PrivateIpAddress", "N/A")
        
#         running_instances.append({
#             "Instance ID": instance_id,
#             "Type": instance_type,
#             "Public IP": public_ip,
#             "Private IP": private_ip
#         })

# # Print the results
# for instance in running_instances:
#     print(instance)
