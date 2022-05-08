import json

import boto3

from modules.tools.logger.logger import logger

log = logger


class S3Client:

    def __init__(self):
        self.s3 = boto3.client('s3')

    def get_names(self, resource_name):
        log.info("Get names from file")
        bucket = 'res-names'
        response = self.s3.get_object(Bucket=bucket, Key=resource_name)
        content = response['Body']
        names = json.loads(content.read()).get('names', [])
        return list(set(names))
