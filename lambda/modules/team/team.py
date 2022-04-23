import random

from modules.config.config import (
    ERROR_TAG,
    ERROR_NOT_ENOUGH_MSG,
    CALC_TEAM_MEMBER_MAX_TRIES,
    ERROR_MAX_TRIES_MSG,
    )

from modules.tools.logger.logger import get_logger


log = get_logger()


def calc_team(team_name, names, names_sel, n_members):
    """Choose n members randomly from a lists of names discarding names already selected from this team or previous teams.
    This implementation retries a max of times the random choose of a member when its name has already been selected.
    Note: Consider to remove each member selected from the original names list in a future implementation.
    """
    log.info(f"Generate team: {team_name}")
    if len(names_sel) + n_members > len(names):
        log.warning(f"{ERROR_TAG}: {team_name}: {ERROR_NOT_ENOUGH_MSG}!")
        return {team_name: (ERROR_TAG, ERROR_NOT_ENOUGH_MSG)}
    members = []
    for _ in range(n_members):
        name = None
        selection_tries = 0
        while not name:
            name = random.choice(names)
            if name in names_sel:
                selection_tries += 1
                log.info(f"Retry {selection_tries:3} when randomly selecting team member. Name already selected: {name}")
                if selection_tries >= CALC_TEAM_MEMBER_MAX_TRIES:
                    log.warning(f"{ERROR_TAG}: {team_name}: {ERROR_MAX_TRIES_MSG}!")
                    return {team_name: (ERROR_TAG, ERROR_MAX_TRIES_MSG % name)}
                name = None
                continue
            names_sel += [name]
            members += [name]
    log.info(f"{team_name} members: {members}")
    return {team_name: members}
