import io,os,boto3
client=boto3.client("s3")
with io.open("input.txt","r",encoding="utf-8")as f1:
    data=f1.read()
    f1.close()
data2=data.split("\n")
pwd=os.getcwd()
for line in data2:
    bucket=line.split(",")[0]
    file_name=line.split(",")[1]
    path=pwd+"/"+file_name
    client.upload_file(path,bucket,file_name)
    print("file uploaded: "+file_name)