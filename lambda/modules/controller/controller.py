from modules.tools.logger.logger import get_logger

log = get_logger()


class EventController:
    def __init__(self, event):
        self.event = event

    def get_teams_to_calculate_raw(self):
        return self.event['teamsToCalculate']

    def get_num_members_for_team_raw(self):
        return self.event['numMembersForTeam']

    def get_teams_to_calculate(self):
        res = self.get_teams_to_calculate_raw()
        return self.sanitize_number(res)

    def get_num_members_for_team(self):
        res = self.get_num_members_for_team_raw()
        return self.sanitize_number(res)

    @staticmethod
    def sanitize_number(number):
        if isinstance(number, (int, float)):
            return int(number)
        if isinstance(number, str) and number.isnumeric():
            return int(number)
        return 0
