import pytest


@pytest.fixture()
def random_choice_names_mock(mocker):
    mocker.patch("random.choice",
                 side_effect=('Rei Ayanami', 'Son Goku', 'Monokuma')
                 )
