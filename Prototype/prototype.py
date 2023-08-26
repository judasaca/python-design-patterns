from copy import deepcopy
from multi_units import Knight, Archer
from abc import ABC, abstractmethod 
class Barracks:
    def __init__(self) -> None:
        self.units = {
            "knight": {
                1: Knight(1),
                2: Knight(2)
            },
            "archer": {
                1: Archer(1),
                2: Archer(2)
            }
        }
        
    def build_unit(self, unit_type, level):
        return self.units[unit_type][level].clone()

b = Barracks()
k = b.build_unit("knight", 1)
a = b.build_unit("archer", 2)
print(k, a)