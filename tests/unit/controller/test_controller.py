from modules.controller.controller import EventController


def test_get_teams_to_calculate(json_event_resource):
    controller = EventController(json_event_resource)
    result = controller.get_teams_to_calculate()
    result_expected = 17
    assert result == result_expected


def test_get_num_members_for_team(json_event_resource):
    controller = EventController(json_event_resource)
    result = controller.get_num_members_for_team()
    result_expected = 3
    assert result == result_expected
