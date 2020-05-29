import boto3
import handler

ec2 = boto3.resource('ec2')
client = boto3.client('ec2')

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_instances
instancesDesc = client.describe_instances(MaxResults=10)

# use first instance you find in the region
instanceId = instancesDesc["Reservations"][0]["Instances"][0]["InstanceId"]
print(instanceId)
instance = ec2.Instance(instanceId)

print(instance.public_ip_address)
print(instance.tags)

# if it has an ip address then its probebly up and can be updated in noip
if instance.public_ip_address is not None:
    handler.update_dns_for_instance(instance)
