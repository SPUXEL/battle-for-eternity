
# CHARACTER


from dataclasses import dataclass


@dataclass
class Item:
    id: int
    name: str
    description: str
    type: str
    value: int | None


@dataclass
class CharacterSlots:
    weapon: Item | None
    armor: Item | None
    artifact_1: Item | None = None
    artifact_2: Item | None = None
    artifact_3: Item | None = None


@dataclass
class CharacterBaseCharacteristics:
    damage: int
    health: int
    armor: int


@dataclass
class CharacterLevel:
    level: int
    experience: int


@dataclass
class Character:
    id: int
    level: CharacterLevel
    base_characteristics: CharacterBaseCharacteristics
    slots: CharacterSlots
    vault: list[Item]
