import boto3
from datetime import datetime, timezone

# Initialize AWS clients
ec2_client = boto3.client("ec2")
sns_client = boto3.client("sns")

# SNS topic ARN (Replace with your SNS ARN)
SNS_TOPIC_ARN = "arn:aws:sns:your-region:your-account-id:your-topic"


def lambda_handler(event, context):
    # Get all running EC2 instances
    instances = ec2_client.describe_instances(
        Filters=[{"Name": "instance-state-name", "Values": ["running"]}]
    )

    alert_instances = []

    # Check each instance
    for reservation in instances["Reservations"]:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            launch_time = instance["LaunchTime"]  # Launch time in UTC
            current_time = datetime.now(timezone.utc)

            # Calculate running days
            running_days = (current_time - launch_time).days

            # Check if the instance has an Elastic IP
            eip_allocations = ec2_client.describe_addresses(
                Filters=[{"Name": "instance-id", "Values": [instance_id]}]
            )

            if eip_allocations["Addresses"] and running_days > 30:
                alert_instances.append(
                    f"Instance {instance_id}  running for {running_days} days."
                )

    # Send SNS notification if any instances are found
    if alert_instances:
        message = "\n".join(alert_instances)
        sns_client.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="EC2 Alert: Instances with EIP Running Over 30 Days",
            Message=message,
        )

        return {"statusCode": 200, "body": "Notification sent!"}

    return {"statusCode": 200, "body": "No instances exceeding the limit."}
