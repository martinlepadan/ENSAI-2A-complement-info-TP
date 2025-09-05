from .abstract_formula_attack import AbstractFormulaAttack

class PhysicalFormulaAttack(AbstractFormulaAttack):

    def get_attack_stat(APkm) -> float:
        return APkm.attack_current

    def get_defense_stat(APkm) -> float:
        return APkm.defense_current