import boto3

client = boto3.client('ecr')

repository_name = 'cloud-native-monitoring-app-repo'

response = client.create_repository(repositoryName = repository_name)

repository_uri = response['repository']['repositoryUri']

print(repository_uri)

# 058264451580.dkr.ecr.us-east-1.amazonaws.com/cloud-native-monitoring-app-repo