from business_object.attack.fixed_damage_attack import FixedDamageAttack
from business_object.pokemon.abstract_pokemon import AbstractPokemon


class MockAbstractPokemonDefender(AbstractPokemon):
    def get_pokemon_attack_coef(self):
        return 0


class MockAbstractPokemonAttacker(AbstractPokemon):
    def get_pokemon_attack_coef(self):
        return 0


class TestFixedDamageAttack:
    def test_compute_damage(self):
        init_power = 20
        fda = FixedDamageAttack(power=init_power)
        power = fda.compute_damage(MockAbstractPokemonAttacker, MockAbstractPokemonDefender)
        assert power == init_power


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
