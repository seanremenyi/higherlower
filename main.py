import art
import game_data
import random
import os

def game():
    score = 0
    first = random.choice(game_data.data)
    
    while True:
        second = random.choice(game_data.data)
        winner = ""
        
        if first['follower_count'] > second['follower_count']:
            winner = "A"
        else:
            winner = "B"

        print(f"{art.logo}\nCompare A: {first['name']}, a {first['description']} from {first['country']}")
        print(f"{art.vs}\nCompare B: {second['name']}, a {second['description']} from {second['country']}")
        
        if input("\nWho do you believe has more instagram followers? A or B? ") == winner:
            os.system("clear")
            score += 1
            first = second
        else:
            os.system("clear")
            print(f"{art.logo}\nYou lost, your score is {score}")
            break
game()