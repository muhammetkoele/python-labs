import boto3
from datetime import datetime

client = boto3.client('s3')
response = client.list_buckets()

print(response)
print("====================================")
#print(response["Buckets"][0]["Name"])

for bucket in response["Buckets"]:
    creation_date = bucket["CreationDate"]
    print(datetime.strftime(creation_date, "%Y-%m-%d %H:%M:%S"), bucket["Name"])

