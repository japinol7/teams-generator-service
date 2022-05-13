from modules.config.config import ERROR_MAX_MSG, BODY_ERRORS_KEY, INPUT_ERROR_TAG, INPUT_ERRORS_KEY
from modules.tools.logger.logger import logger as log


def log_wrong_input_values(controller):
    error_msg = ERROR_MAX_MSG + f" Asked for : {controller.get_teams_to_calculate_raw()} teams " \
                                f"and {controller.get_num_members_for_team_raw()} members."
    log.info(error_msg)
    return {BODY_ERRORS_KEY: {
                INPUT_ERRORS_KEY: [[INPUT_ERROR_TAG, error_msg]],
                }
            }
