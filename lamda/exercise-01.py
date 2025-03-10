import json


def lambda_handler(event, context):
    # Extract name from the event
    name = event.get("name", "World")

    # Create a response
    response = {"statusCode": 200, "body": json.dumps(f"Hello, {name}!")}

    return response
