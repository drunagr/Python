players = [{"name": "jim", "money": 5000}, {"name": "jim1", "money": 3100}, {"name": "jim2", "money": 3100}]
player_name = "jim"
money = 23000
for players_dict in players:
    for v in players_dict.values():
        if v  == player_name:
            players_dict["money"] = money

print(players)
