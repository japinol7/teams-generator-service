from modules.config.config import ERROR_MAX_MSG
from modules.tools.logger.logger import logger

log = logger


def log_wrong_input_values(controller):
    error_msg = ERROR_MAX_MSG + f" Asked for : {controller.get_teams_to_calculate_raw()} teams " \
                                f"and {controller.get_num_members_for_team_raw()} members."
    log.info(error_msg)
    return error_msg
