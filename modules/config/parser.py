import os

from collections import namedtuple
from modules.aws.ssm_client import SSMParamClient

ConfigVars = namedtuple('config_vars', ['environ', 'ssm'])
CONFIG_VARS = {
    'teams_gen_file_contestants': ConfigVars('TEAMS_GEN_FILE_CONTESTANTS', 'teams-gen-file-contestants'),
    'teams_gen_file_teams': ConfigVars('TEAMS_GEN_FILE_TEAMS', 'teams-gen-file-teams'),
    }


class ConfigParser:
    """Represents a configuration parser.
    Loads variables from the environment when available; otherwise it loads them from SSM.
    """

    def __init__(self):
        self._config = {}
        ssm = SSMParamClient()
        for cv, vals in CONFIG_VARS.items():
            self._config.update({
                    cv: os.environ.get(vals.environ) or ssm.get(vals.ssm)
                    })

    def __getitem__(self, item):
        return self._config[item]

    def get(self, item, default=None):
        return self.__getitem__(item) or default
