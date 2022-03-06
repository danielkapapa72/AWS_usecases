"""
import boto3

ec2_client = boto3.client("ec2")
print(ec2_client.describe_instances())
data = ec2_client.describe_instances()
data = data["Reservations"]
print(data.keys())
#ec2_client.stop_instances(InstanceIds=[
#         'i-083c12e838faf54b7', 'i-06e8bff6db25aa20a'
#     ])
"""
# How to obtain the EC2 ID and stop running instance without manually passing the instance id
import boto3,sys
#initialize ec2 client object
ec2_client=boto3.client("ec2")
#getting all ec2 instance info
data=ec2_client.describe_instances()
#getting info from root key 
data=data["Reservations"]
#iteration from the output of above 
for xx in data:
    instances=xx["Instances"]
    for instance in instances:
        #getting instance id from inner key
        print(instance["InstanceId"])
        print("__________")
# Stop instances
        #ec2_client.terminate_instances(InstanceIds=[
            #'i-0fc2b090dd8f55923', 'i-04fd12d82e3d4fab8', 'i-0f345965638a59d96', 'i-00cd1195f1b36e60d', 'i-003185e5a76f98133', 'i-0cc3e1ed5466b847c', 'i-0162a18f6ccf8d475', 'i-07127ddfd28cd50ee', 'i-05ba8f324de966cf2', 'i-0fba3c8c5dd6ba444'
            #])
