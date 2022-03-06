import boto3

ec2_resource = boto3.resource("ec2")
# create 10 instances without changing the parameters create_instance: Homework-day1
# The for loops will helps us to execute our code by creating Ec2 10 times 
for i in range(0,2):
    response = ec2_resource.create_instances(ImageId='ami-0c293f3f676ec4f90',
                             InstanceType="t2.micro",
                             MaxCount=1,
                             SubnetId='subnet-0c3eaca45f8d8eaf4',
                             MinCount=1)
    print(response)