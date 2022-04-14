from modules.team.team import calc_team


def test_calc_team_1_member(team_names_resource, random_choice_names_mock):
    result = calc_team(team_name='Team_01', names=team_names_resource, names_sel=[], n_members=1)
    result_expected = {'Team_01': ['Rei Ayanami']}
    assert result == result_expected


def test_calc_team_3_members(team_names_resource, random_choice_names_mock):
    result = calc_team(team_name='Team_01', names=team_names_resource, names_sel=[], n_members=3)
    result_expected = {'Team_01': ['Rei Ayanami', 'Son Goku', 'Monokuma']}
    assert result == result_expected


def test_calc_team_no_members(team_names_resource, random_choice_names_mock):
    result = calc_team(team_name='Team_01', names=team_names_resource, names_sel=[], n_members=0)
    result_expected = {'Team_01': []}
    assert result == result_expected


def test_calc_team_not_enough_names(random_choice_names_mock):
    result = calc_team(team_name='Team_01', names=['Name1', 'Name2'], names_sel=[], n_members=3)
    result_expected = {'Team_01': ('Error', 'Not enough Characters to generate this team')}
    assert result == result_expected
