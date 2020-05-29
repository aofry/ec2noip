import json
import boto3
import os
import noip

username = os.getenv('NOIP_USER')
password = os.getenv('NOIP_PASS')
domain = os.getenv('NOIP_DOMAIN')
ec2 = boto3.resource('ec2')


def start(event, context):
    instance = ec2.Instance(event['detail']['instance-id'])
    # print("Got event for instance: " + instance['detail'])
    # instance = ec2.Instance('i-0f3bab323gs346bbef')
    print(instance.public_ip_address)
    print(instance.tags)
    print(domain)

    tag_name = update_dns_for_instance(instance)

    body = {
        "tag": tag_name,
        "ip": instance.public_ip_address,
        "username": username
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


def update_dns_for_instance(instance):
    tag_name = ""
    # if tag was placed on the instance, we can know the full domain name to set in noip
    if None not in (instance.tags, domain, username, password, instance.public_ip_address):
        tag_name = instance.tags[0]['Value']
        noip.update_dns((username, password, tag_name + "." + domain, instance.public_ip_address))
    return tag_name
