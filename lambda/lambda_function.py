import json
import random

import boto3

from modules.config.config import (
    SERVICE_NAME,
    N_TEAMS,
    N_MEMBERS,
    BODY_TEAMS_KEY,
    BODY_ERRORS_KEY,
    ERROR_TAG,
    ERROR_NOT_ENOUGH_MSG,
    )
from modules.tools.logger import logger
from modules.version import version

log = logger.get_logger()


def load_names():
    log.info("Get names from file")
    s3 = boto3.client('s3')
    bucket = 'res-names'
    key = 'names_anime1.json'
    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body']
    return json.loads(content.read()).get('names', [])


def calc_team(team_name, names, names_sel, n_members):
    log.info(f"Generate team: {team_name}")
    if len(names_sel) + n_members > len(names):
        log.warning(f"Error: {team_name}: {ERROR_NOT_ENOUGH_MSG}!")
        return {team_name: (ERROR_TAG, ERROR_NOT_ENOUGH_MSG)}
    members = []
    for _ in range(n_members):
        name = None
        while not name:
            name = random.choice(names)
            if name in names_sel:
                name = None
                continue
            names_sel += [name]
            members += [name]
    log.info(f"{team_name} members: {members}")
    return {team_name: members}


def lambda_handler(event, context):
    log.info(f"Start service {SERVICE_NAME} version: {version.get_version()}")

    names_sel = []
    names = list(set(load_names()))

    body = {BODY_TEAMS_KEY: {}, BODY_ERRORS_KEY: {}}
    for i in range(N_TEAMS):
        team_name = f'Team {i + 1}'
        team = calc_team(team_name, names, names_sel, N_MEMBERS)
        body_key = BODY_TEAMS_KEY if team.get(team_name)[0] != ERROR_TAG else BODY_ERRORS_KEY
        body[body_key].update(team)

    log.info(f"End service {SERVICE_NAME}")
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(body),
        }


if __name__ == "__main__":
    res = lambda_handler(event=None, context=None)
    log.info(res['body'])
