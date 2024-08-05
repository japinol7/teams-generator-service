import io
import json

import boto3

from modules.tools.logger.logger import logger as log


class S3Client:

    def __init__(self):
        self.s3 = boto3.client('s3')
        self.bucket = 'teams-generator'

    def get_contestants(self, resource_name, remove_duplicates=True, sorted_=True):
        log.info("Get contestants from bucket")
        response = self.s3.get_object(Bucket=self.bucket, Key=resource_name)
        content = response['Body']
        names = json.loads(content.read()).get('names', [])
        if remove_duplicates:
            names = list(set(names))
        if sorted_:
            names = sorted(names)
        return names

    def upload_teams(self, resource_name, body):
        log.info("Upload teams to bucket")
        res = self.s3.upload_fileobj(io.BytesIO(body.encode("utf-8")), Bucket=self.bucket, Key=resource_name)
        return res
