import random

from modules.config.config import (
    ERROR_TAG,
    ERROR_NOT_ENOUGH_MSG,
    )

from modules.tools.logger.logger import get_logger


log = get_logger()


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
