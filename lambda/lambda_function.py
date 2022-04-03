import json
import random

from modules.config.config import (
    SERVICE_NAME,
    N_MEMBERS_MAX,
    N_TEAMS_MAX,
    ERROR_MAX_MSG,
    BODY_TEAMS_KEY,
    BODY_ERRORS_KEY,
    ERROR_TAG,
    ERROR_NOT_ENOUGH_MSG,
    )
from modules.config.parser import ConfigParser
from modules.controller.controller import EventController
from modules.aws.s3_client import S3Client
from modules.tools.logger import logger
from modules.tools.utils.utils import read_file_as_string
from modules.version import version

log = logger.get_logger()


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

    controller = EventController(event)
    num_teams = controller.get_teams_to_calculate()
    num_members = controller.get_num_members_for_team()
    if num_teams > N_TEAMS_MAX or num_members > N_MEMBERS_MAX or num_teams < 1 or num_members < 1:
        error_msg = ERROR_MAX_MSG + f" Asked for : {controller.get_teams_to_calculate_raw()} teams " \
                                    f"and {controller.get_num_members_for_team_raw()} members."
        log.info(error_msg)
        log.info(f"End service {SERVICE_NAME}")
        return {
            'statusCode': 200,
            'body': json.dumps(error_msg),
        }

    config_parser = ConfigParser()
    res_file_names_anime = config_parser['file_names_anime_1']

    s3 = S3Client()
    names = s3.get_names(res_file_names_anime)

    names_sel = []
    body = {BODY_TEAMS_KEY: {}, BODY_ERRORS_KEY: {}}
    log.info(f"Generate {num_teams} Teams of {num_members} members")
    for i in range(num_teams):
        team_name = f'Team {i + 1}'
        team = calc_team(team_name, names, names_sel, num_members)
        body_key = BODY_TEAMS_KEY if team.get(team_name)[0] != ERROR_TAG else BODY_ERRORS_KEY
        body[body_key].update(team)

    log.info(f"End service {SERVICE_NAME}")
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(body),
        }


if __name__ == "__main__":
    event_json = read_file_as_string('events/event.json')
    res = lambda_handler(event=json.loads(event_json), context=None)
    log.info(res['body'])
