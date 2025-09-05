from business_object.pokemon.abstract_pokemon import AbstractPokemon


class MockAbstractPokemon(AbstractPokemon):
    def get_pokemon_attack_coef(self):
        return 0


class TestLevelUpPokemon:
    def test_level_up(self):
        missingno = MockAbstractPokemon()
        missingno.level_up()
        assert missingno.level == 1


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
