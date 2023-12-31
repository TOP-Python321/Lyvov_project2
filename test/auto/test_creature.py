from model.creature import Maturity, Creature, Kind, Health, Hunger
import pytest


@pytest.mark.parametrize('kind, name', [(Kind.CAT, "Monty"), (Kind.CAT, "5986")])
def test_creature_init(kind, name):
    creature = Creature(kind, name)
    assert creature.name == name
    assert creature.mature == Maturity.CUB
    assert creature.params[Health].value == 10
    assert creature.params[Hunger].value == 5


@pytest.mark.parametrize('health, hunger', [(9.5, 4.0)])
def test_creature_update(health, hunger):
    creature = Creature(Kind.CAT, "Monty")
    creature.update()
    assert creature.params[Health].value == health
    assert creature.params[Hunger].value == hunger


@pytest.mark.parametrize('maturity, health, hunger',
                         [(Maturity.YOUNG, (0, 50), (0, 30)),
                         (Maturity.ADULT, (0, 45), (0, 25)),
                         (Maturity.OLD, (0, 35), (0, 20))])
def test_creature_grow_up(maturity, health, hunger):
    creature = Creature(Kind.CAT, "Monty")
    creature._grow_up(maturity)
    assert creature.params[Health].range == health
    assert creature.params[Hunger].range == hunger


@pytest.mark.parametrize('value, min_, max_, expected',
                         [(5, 0, 25, 4.0),
                         (0, 0, 30, 0),
                         (0, 0, 25, 0),
                         (0, 0, 20, 0)])
def test_hunger_update(value, min_, max_, expected):
    creature = Creature(Kind.CAT, "Monty")
    hunger = Hunger(value, min_, max_, creature)
    hunger.update()
    assert hunger.value == expected


@pytest.mark.parametrize('value, min_, max_, expected',
                         [(10, 0, 20, 9.5),
                          (0, 0, 50, 0),
                          (0, 0, 45, 0),
                          (0, 0, 35, 0)])
def test_health_update(value, min_, max_, expected):
    creature = Creature(Kind.CAT, "Monty")
    health = Health(value, min_, max_, creature)
    health.update()
    assert health.value == expected