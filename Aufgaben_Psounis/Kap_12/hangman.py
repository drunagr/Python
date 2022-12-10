import random as rnd

with open("C:\\Users\\dpoly\\Desktop\\PYTHON\\Python Psounis\\Kap_12\\worte.txt") as f:
    wort = rnd.choice([w.strip().upper() for w in f])
    print()
    #print(wort)
versuche = 8
gesucht = set(b for b in wort)
geraten = set()
while versuche > 0:
    text = f"noch{versuche:>2} Versuche: "
    text += " ".join([f"{b if b in geraten else '_'}" for b in wort])
    versuch = input(text + " ihr Buchstabe? ").upper()
    geraten.add(versuch)
    if versuch not in gesucht: versuche -= 1
    if gesucht.issubset(geraten): break
text = "Gewonnen! " if versuche > 0 else "Verloren! "
print(text + "Das  gesuchte Wotrt war:", wort)
