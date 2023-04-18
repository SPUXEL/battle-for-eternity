
from utils import monster


monsters = monster.Monsters([

    monster.Monster(
        name="Гоблин-командир",
        description="",
        basic_characteristics=monster.MonsterBasicCharacteristics(
            damage=15,
            health=50,
            armor=25
        )
    ),

    monster.Monster(
        name="Троль вояка",
        description="",
        basic_characteristics=monster.MonsterBasicCharacteristics(
            damage=20,
            health=55,
            armor=25
        )
    )

])
