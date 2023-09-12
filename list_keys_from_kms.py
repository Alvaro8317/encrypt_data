import json
import boto3
client = boto3.client('kms')
response = client.list_keys(Limit=123)
print(json.dumps(response, indent=2))