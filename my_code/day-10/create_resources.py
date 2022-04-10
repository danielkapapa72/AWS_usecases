import boto3
client = boto3.client('ec2')
resource = boto3.resource('ec2')
vpc = client.create_vpc(CidrBlock='192.168.1.0/24')
vpcid = resource.Vpc(vpc["Vpc"]["VpcId"])
vpcid.create_tags(Tags=[{"Key": "Name", "Value": "custom1"}])
igInit = client.create_internet_gateway(TagSpecifications=[{'ResourceType': 'internet-gateway','Tags': [{"Key": "Name", "Value": "IGW-demo"}]},])
igId = igInit["InternetGateway"]["InternetGatewayId"]
#Attach Internet Gateway to VPC
vpcid.attach_internet_gateway(InternetGatewayId=igId)
#Create Routing Table
routeTable = vpcid.create_route_table()
#Create public route
route = routeTable.create_route(DestinationCidrBlock='0.0.0.0/0',GatewayId=igId)
routeTable.create_tags(Tags=[{"Key": "Name", "Value": "rt-01"}])
#Create Subnet
subnet = vpcid.create_subnet(CidrBlock='192.168.1.0/24')
subnet.create_tags(Tags=[{"Key": "Name", "Value": "sub01"}])
#Associate subnet with public route table
routeTable.associate_with_subnet(SubnetId=subnet.id)
#Create Security Group
secGroup = resource.create_security_group(GroupName='kapsdemo', Description='EC2 Security Group', VpcId=vpcid.id)
#Ingress Rule
secGroup.authorize_ingress(IpPermissions=[{'FromPort': 22,'IpProtocol': 'tcp','IpRanges': [{'CidrIp': '0.0.0.0/0','Description': 'SSH Access'},],'ToPort': 22,},])