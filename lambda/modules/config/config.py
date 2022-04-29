from modules.version import version

SERVICE_NAME = 'teams_generator'

N_TEAMS_MAX = 50
N_MEMBERS_MAX = 15

BODY_TEAMS_KEY = 'teams'
BODY_ERRORS_KEY = 'errors'

ERROR_TAG = 'Error'
ERROR_MAX_MSG = f"User input Error. Maximum {N_TEAMS_MAX} teams and {N_MEMBERS_MAX} members for team. " \
                f"Values must be numbers!"
ERROR_NOT_ENOUGH_MSG = 'Not enough Characters to generate this team'

CALC_TEAM_MEMBER_MAX_TRIES = 100
ERROR_MAX_TRIES_MSG = f"Max tries exceeded while choosing a team member: {CALC_TEAM_MEMBER_MAX_TRIES}. Name: %s"

LOG_START_SERVICE_MSG = f"Start service {SERVICE_NAME} version: {version.get_version()}"
LOG_END_SERVICE_MSG = f"End service {SERVICE_NAME}"
