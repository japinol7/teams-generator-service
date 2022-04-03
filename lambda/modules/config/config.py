SERVICE_NAME = 'teams_generator'

N_TEAMS_MAX = 50
N_MEMBERS_MAX = 15

BODY_TEAMS_KEY = 'teams'
BODY_ERRORS_KEY = 'errors'

ERROR_TAG = 'Error'
ERROR_MAX_MSG = f"User input Error. Maximum {N_TEAMS_MAX} teams and {N_MEMBERS_MAX} members for team. " \
                f"Values must be numbers!"
ERROR_NOT_ENOUGH_MSG = 'Not enough Characters to generate this team'
