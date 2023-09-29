from model.creature import Maturity, Creature, Kind, Health, Hunger
import pytest


@pytest.mark.parametrize('kind, name', [(Kind.CAT, "Ovca"), (Kind.CAT, "1234")])
def test_creature_init(kind, name):
    creature = Creature(kind, name)
    assert creature.name == name
    assert creature.mature == Maturity.CUB
    assert creature.params[Health].value == 10
    assert creature.params[Hunger].value == 5