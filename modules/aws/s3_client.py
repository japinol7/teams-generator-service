import json

import boto3

from modules.tools.logger.logger import logger as log


class S3Client:

    def __init__(self):
        self.s3 = boto3.client('s3')
        self.bucket = 'res-names'

    def get_contestants(self, resource_name):
        log.info("Get contestants from bucket")
        response = self.s3.get_object(Bucket=self.bucket, Key=resource_name)
        content = response['Body']
        names = json.loads(content.read()).get('names', [])
        return list(set(names))
