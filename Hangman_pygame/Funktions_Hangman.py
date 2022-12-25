import os
import random



def write_score(name, score):
    with open("high_score.txt", "w") as f:
        f.write(f"{name} {score}")

def read_score():
    if os.path.exists("high_score.txt"):
        with open("high_score.txt", "r") as f:
            name, score = f.read().capitalize().split(" ")   
        return name, int(score)
    return "", 0



def word_pick_easy():
    with open("words_Hangman.txt") as f:
        word =  random.choice([w.strip().lower().split(" ")[0] for w in f])
        #for testing
        print(word)
    return word

def word_pick_noteasy():
    with open("Teil_58_Wörter.txt") as f:
        word =  random.choice([w.strip().lower().split(" ")[0] for w in f])
        #for testing
        print(word)
    return word
