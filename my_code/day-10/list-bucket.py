#list and print the name of available buckets
import boto3
client=boto3.client("s3")
data=client.list_buckets()
#get the keys from json by doing data.keys()
#print(data.keys())
buckets=data["Buckets"]
for bucket in buckets:
    print(bucket["Name"])