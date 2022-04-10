import boto3
ec2_client = boto3.resource("ec2")
#response=ec2_client.create_instances(ImageId="ami-0c02fb55956c7d316",InstanceType="t2.micro",MaxCount=1,MinCount=1,VpcId="vpc-0dea912da99246ed9")
#print("response")
for i in range(0,3):
    response=ec2_client.create_instances(
               ImageId = 'ami-0c02fb55956c7d316',
               InstanceType ='t2.micro', MaxCount = 1, MinCount = 1,
               NetworkInterfaces = [{'SubnetId': "subnet-0238dcd0eaffa6f2a",
               'DeviceIndex': 0, 'AssociatePublicIpAddress':
               True, 'Groups': ["sg-0b8c781402ec7881d"]}])
    print(response)
