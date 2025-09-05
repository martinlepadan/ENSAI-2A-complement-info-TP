from business_object.attack.fixed_damage_attack import FixedDamageAttack

class TestFixedDamageAttack:
    def test_compute_damage(self):
        init_power=20
        fda = FixedDamageAttack(power=init_power)
        power = fda.compute_damage()
        assert power == init_power


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
