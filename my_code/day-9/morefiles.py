# import all files by using glob
import glob, boto3 
s3=boto3.client('s3')
static_path="C:\\Users\\kdang\\OneDrive\\Desktop\\exec-day6\\"
bucket_name="mytrainingkaps"
files=glob.glob(static_path+"*.*")
for xx in files:
    file_name=xx.split("\\")[-1]
    s3.upload_file(xx,bucket_name,file_name)
    print("My code does not have error")
    
    
"""
#upload all files from a directory 

import glob,boto3
client=boto3.client("s3")
#identify what are the files there in the directory 
static_path="/Users/ronidas/Desktop/files/"
bucket_name="roni-test"
#*.* means any extension or all files
#this gives you a list , every element of the list will be single file
# variable files is holding the list
files=glob.glob("/Users/ronidas/Desktop/files/"+"*.*")
for file in files:
    file_name=file.split("/")[-1]
    client.upload_file(file,bucket_name,file_name)
    print("succesfully uploaded: "+file_name)

"""