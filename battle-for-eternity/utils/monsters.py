
from utils import monster


monsters = monster.Monsters([

    monster.Monster(
        name="Гоблин-командир",
        description="",
        basic_characteristics=monster.MonsterBasicCharacteristics(
            damage=7,
            health=50,
            armor=35
        )
    ),

    monster.Monster(
        name="Троль вояка",
        description="",
        basic_characteristics=monster.MonsterBasicCharacteristics(
            damage=5,
            health=55,
            armor=40
        )
    )

])
