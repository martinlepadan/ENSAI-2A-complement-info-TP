from .abstract_attack import AbstractAttack


class FixedDamageAttack(AbstractAttack):
    def compute_damage(self, APkm, DAPkm) -> int:
        """
        Compute the damage of an attack

        Returns :
            int : the damage
        """
        return self.power
