import boto3


def fetch() -> dict:
    client_ec2 = boto3.client('ec2', region_name='ap-northeast-1')
    response = client_ec2.describe_instances(
        Filters=[
            {'Name': 'instance-state-name',
             'Values': [
                 'running',
             ]
             },
        ],
    )

    print(response)

fetch()