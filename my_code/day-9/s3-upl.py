import boto3
day6=boto3.client('s3')
path="C:\\Users\\kdang\\OneDrive\\Desktop\\exec-day6\\Screenshot_1.png"
day6.upload_file(path, "mytrainingkaps", "kaps-screensht.png")