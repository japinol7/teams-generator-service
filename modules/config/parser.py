import os

from collections import namedtuple
from modules.aws.ssm_client import SSMParamClient

ConfigVars = namedtuple('config_vars', ['environ', 'ssm'])
CONFIG_VARS = {
    'file_names_anime_1': ConfigVars('FILE_NAMES_ANIME_1', 'file-names-anime-1'),
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
