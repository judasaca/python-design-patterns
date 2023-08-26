from abc import ABC, abstractmethod
from copy import deepcopy
import json



class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class Concrete(Prototype):
    def clone(self):
        return deepcopy(self)
    

class Knight(Prototype):
    def __init__(self, level: int) -> None:
        self.unit_type = "Knight"
        with open(f'{self.unit_type}.json', 'r', encoding="utf-8") as jsonfile:
            data = json.loads(jsonfile.read()).get(f'{level}')
            self.life = data.get("life")
            self.speed = data.get("speed")
            self.attack_power = data.get("attack_power")
            self.attack_range = data.get("attack_range")
            self.weapon = data.get("weapon")

    def __str__(self):
        r= f"""
Type: {self.life}
Speed: {self.speed}
Attack power: {self.attack_power}
Attack range: {self.attack_range}
Wapon: {self.weapon}
        """
        return r
    def clone(self):
        return deepcopy(self)

class Archer(Prototype):
    def __init__(self, level: int) -> None:
        self.unit_type = "Archer"
        with open(f'{self.unit_type}.json', 'r', encoding="utf-8") as jsonfile:
            data = json.loads(jsonfile.read()).get(f'{level}')
            self.life = data.get("life")
            self.speed = data.get("speed")
            self.attack_power = data.get("attack_power")
            self.attack_range = data.get("attack_range")
            self.weapon = data.get("weapon")

    def __str__(self):
        r= f"""
Type: {self.life}
Speed: {self.speed}
Attack power: {self.attack_power}
Attack range: {self.attack_range}
Wapon: {self.weapon}
        """
        return r
    
    def clone(self):
        return deepcopy(self)