from random import randint

from ABC import abstractmethod

from .abstract_attack import AbstractAttack


class AbstractFormulaAttack(AbstractAttack):
    @abstractmethod
    def get_attack_stat(APkm) -> float:
        pass

    @abstractmethod
    def get_defense_stat(APkm) -> float:
        pass

    def compute_damage(self, APkm, DAPkm) -> int:
        rand = randint(85, 100) / 100
        power = self._power
        attack = self.get_attack_stat(APkm)
        defense = self.get_defense_stat(DAPkm)
        level = APkm.level
        base_damage = ((((2 * level) / 5 + 2) * power * attack) / defense * 50) + 2
        return int(base_damage * rand)
