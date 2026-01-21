import boto3

class SecretManagerClient:


    def __init__(self, boto3_client):
        client = boto3_client or boto3.client(AWS.SECRETMANAGER)

