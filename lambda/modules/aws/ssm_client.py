import boto3

from modules.tools.logger.logger import get_logger

log = get_logger()


class SSMParamClient:

    def __init__(self):
        self.ssm = boto3.client('ssm')

    def get(self, key):
        log.debug(f'Retrieve SSM parameter with key {key}')
        res = self.ssm.get_parameter(Name=key, WithDecryption=True)
        return res['Parameter']['Value']
