
from utils import character


character = character.Character(
    id=999,
    level=character.CharacterLevel(
        level=1,
        experience=0
    ),
    base_characteristics=character.CharacterBaseCharacteristics(
        damage=10,
        health=100,
        armor=100
    ),
    slots=character.CharacterSlots(
        weapon=character.Item(
            id=1,
            name="Дубовая ветка",
            description="",
            type="weapon",
            value=20
        ),
        armor=character.Item(
            id=2,
            name="Доспехи моего деда",
            description="",
            type="armor",
            value=40
        )
    ),
    vault=[
        character.Item(
            id=1,
            name="Дубовая ветка",
            description="",
            type="weapon",
            value=20
        ),
        character.Item(
            id=3,
            name="Ржавый меч",
            description="",
            type="weapon",
            value=30
        ),
        character.Item(
            id=2,
            name="Доспехи моего деда",
            description="",
            type="armor",
            value=40
        )
    ]
)
