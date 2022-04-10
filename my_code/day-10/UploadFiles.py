import boto3
client=boto3.client("s3")
source_bucket="kapproject"
destination="mytrainingkaps"
response=client.copy_object(
    Bucket=destination,
    CopySource={'Bucket':source_bucket, 'Key': 'receiver.yaml'},
    Key="nested.yaml"
   )
print(response)
"""
#upload one file from source bucket to destination bucket
import boto3
client=boto3.client("s3")
#this is the bucket where alreday have the file
source_bucket="roni-test"
#this is the bucket where we are going to copy our file
target_bucket="roni-test1"

response=client.copy_object(
    Bucket=target_bucket,
    CopySource={'Bucket': source_bucket, 'Key': 'upload1.png'}, #this is the info about source bucket and already uoloaded file
    Key="copy.png",
   )
print(response)

"""
    