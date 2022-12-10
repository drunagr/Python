import json


def init_paixtes_data() -> object:
    try:
        with open("paixtes.json") as f:
            players = json.load(f)
            # print(players)
            # print(len(players))
    except FileNotFoundError:
        players = []
    return players


def save_paixtes_status(onoma) -> object:
    with open("paixtes.json", "w") as f:
        json.dump(onoma, f)




def main():
    players = init_paixtes_data()
    # print(type(players))
    while True:
        print("1-new player")
        print("2-old player")

        choice = int(input("Pick one: "))

        if choice == 1:
            player = {}
            player["name"] = input("Give full name: ")
            player["money"] = 5000
            players.append(player)
            save_paixtes_status(players)
        elif choice == 2:
            player_name = input("What's your name?: ")
            for i in range(len(players)):
                lexiko_i = dict(players[i])
                if player_name in lexiko_i.values():
                    geld = lexiko_i.get("money")



if __name__ == '__main__':
    main()