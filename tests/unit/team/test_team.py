from modules.team.team import calc_team

TEAM_NAME_ARBITRARY = 'Team_01'
ERROR_RES_NOT_ENOUGH_CHARACTERS = {TEAM_NAME_ARBITRARY: ('Error', 'Not enough Characters to generate this team')}


def test_calc_team_1_member(team_names_resource, random_choice_names_mock):
    result = calc_team(team_name=TEAM_NAME_ARBITRARY, names=team_names_resource, names_sel=[], n_members=1)
    result_expected = {TEAM_NAME_ARBITRARY: ['Rei Ayanami']}
    assert result == result_expected


def test_calc_team_3_members(team_names_resource, random_choice_names_mock):
    result = calc_team(team_name=TEAM_NAME_ARBITRARY, names=team_names_resource, names_sel=[], n_members=3)
    result_expected = {TEAM_NAME_ARBITRARY: ['Rei Ayanami', 'Son Goku', 'Monokuma']}
    assert result == result_expected


def test_calc_team_no_members(team_names_resource, random_choice_names_mock):
    result = calc_team(team_name=TEAM_NAME_ARBITRARY, names=team_names_resource, names_sel=[], n_members=0)
    result_expected = {TEAM_NAME_ARBITRARY: []}
    assert result == result_expected


def test_calc_team_not_enough_names():
    result = calc_team(team_name=TEAM_NAME_ARBITRARY, names=['Name1', 'Name2'], names_sel=[], n_members=3)
    result_expected = ERROR_RES_NOT_ENOUGH_CHARACTERS
    assert result == result_expected


def test_calc_team_not_enough_names_already_sel():
    """Test selecting 3 names from a list of 3 names, one of them already selected."""
    result = calc_team(team_name=TEAM_NAME_ARBITRARY,
                       names=['Name1', 'Name2', 'Name3'],
                       names_sel=['Name2'],
                       n_members=3)
    result_expected = ERROR_RES_NOT_ENOUGH_CHARACTERS
    assert result == result_expected
