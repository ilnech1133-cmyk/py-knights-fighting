from app.knights import KNIGHTS
from app.battle_preparation import prepare_knight
from app.battle import fight


def battle(knights_config: dict) -> dict:
    lancelot = knights_config["lancelot"]
    arthur = knights_config["arthur"]
    mordred = knights_config["mordred"]
    red_knight = knights_config["red_knight"]

    prepare_knight(lancelot)
    prepare_knight(arthur)
    prepare_knight(mordred)
    prepare_knight(red_knight)
    # BATTLE:
    # 1 Lancelot vs Mordred:
    fight(lancelot, mordred)
    # 2 Arthur vs Red Knight:
    fight(arthur, red_knight)
    # Return battle results:
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(KNIGHTS))
