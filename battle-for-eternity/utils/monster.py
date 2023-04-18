
from dataclasses import dataclass


@dataclass
class MonsterBasicCharacteristics:
    damage: int
    health: int
    armor: int


@dataclass
class Monster:
    name: str
    description: str
    basic_characteristics: MonsterBasicCharacteristics


@dataclass
class Monsters:
    monsters: list[Monster]
