import boto3

s3_client=boto3.client('s3')
s3_client.upload_file("document.txt", "mytrainingkaps", "important-document.txt")
print("MFile uploaded")