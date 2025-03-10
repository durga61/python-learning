import boto3

ssm = boto3.client("ssm", region_name="ap-south-1")

# Get a single parameter
response = ssm.get_parameter(Name="/company/dev/db-url", WithDecryption=True)
print(response)
print(response["Parameter"]["Value"])

# Get multiple parameters
response = ssm.get_parameters(
    Names=["/company/dev/db-url", "/company/dev/db-password"], WithDecryption=True
)
for param in response["Parameters"]:
    print(f"{param['Name']}: {param['Value']}")


list = [1, 2, 3, 4, 59, 6, 7, 8, 9, 10]
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
dict = {"name": "Alice", "age": 25}

person = {"name": "Alice", "age": 25}
print(f'{person["name"]}: {person["age"]}')
for i in list:
    print(i)

for i in tup:
    print(i)

for key, value in dict.items():
    print(f"{key}: {value}")
