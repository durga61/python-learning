import boto3


def create_s3_bucket(bucket_name):

    client = boto3.client("s3")

    try:
        response = client.create_bucket(
            Bucket="dp-aws-bucket-1",
            CreateBucketConfiguration={"LocationConstraint": "ap-south-1"},
        )
        print(f"Bucket {bucket_name} created successfully")
    except Exception as e:
        print("An error occurred:", e)


def get_bucket_acl(bucket_name):
    client = boto3.client("s3")
    response = client.get_bucket_acl(Bucket=bucket_name)
    print(response)


if __name__ == "__main__":
    bucket_name = "dp-aws-bucket-1"
    # create_s3_bucket(bucket_name)
    get_bucket_acl(bucket_name)
