power_mapping = {0: "low", 1: "medium", 2: "high"}

claws_attacking_power_multiplier = {"low": 2, "medium": 3, "high": 3}

teeth_attacking_power_additive = {"low": 3, "medium": 6, "high": 9}

leg_action_mapping = {0: ["crawling"], 1: ["hopping"], 2: ["walking", "running"]}

wing_action_mapping = {0: [], 1: [], 2: ["flying"]}

names = {
    "wing_name": "WINGS",
    "leg_name": "LEGS",
    "claw_name": "CLAWS",
    "teeth_name": "TEETH",
}

MOVABLE = "MOVABLE"
ATTACKER = "ATTACKER"
body_part_type = {"attacker_name": ATTACKER, "movable_name": MOVABLE}

movement_type = {
    "crawling": {"requires_stamina": 0, "uses_stamina": 1, "speed": 1},
    "hopping": {"requires_stamina": 20, "uses_stamina": 2, "speed": 2},
    "walking": {"requires_stamina": 40, "uses_stamina": 2, "speed": 4},
    "running": {"requires_stamina": 60, "uses_stamina": 4, "speed": 6},
    "flying": {"requires_stamina": 80, "uses_stamina": 4, "speed": 8},
}
