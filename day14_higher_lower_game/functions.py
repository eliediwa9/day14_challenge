# **************** comparing two items in terms of the numbers of instagram ****************

# Functional requirements
# 1 Prompt player to enter name
# 2 Save name of the player and his score
# 3 If player already exists, confirm that he want to continue with old score level
# 4 clear screen and launch game
# 5 Display question and prompt user to answer
# 6 Update score if correct, not if wrong
# 7 Clean the screen and repeat unless user end game

# Imporing modules
import pandas as pd
import random as rd
import os
ALREADY_ASKED = []


# 1

def load_logo():
    from ascii_art import logo
    display = f"{logo}"
    print(display)


def user_info():
    name = input("Enter your name: ").strip()
    return name


# 2
def existing_record(name):
    database = pd.read_csv("player_database.csv")
    if name in database.Player.unique():
        return True
    else:
        return False


def save_newrecord(name):
    with open("player_database.csv", mode="a") as dtb:
        dtb.write(f"\n{name},0")


# 3
def load_database(name, existing):
    database = pd.read_csv("player_database.csv")

    def initialize_game():
        if existing is True:
            prompt = input("Do you want to continue where you left? (y/n):\n").strip()
            if prompt == "n":
                database.loc[database.Player == name, "Score"] = 0
                database.to_csv("player_database.csv", index=False)

        return database

    return initialize_game()


# 4
def clear_screen():
    os.system("clear")


# 5
def prompt_question(data, score):
    global ALREADY_ASKED
    choices = rd.choices(range(len(data)), k=2)
    while choices in ALREADY_ASKED:
        choices = rd.choices(range(len(data)), k=2)

    ALREADY_ASKED.append(choices)
    account_a = data[choices[0]]
    account_b = data[choices[1]]

    def compose_question():
        from ascii_art import vs

        part1 = f"A: {account_a['name']}, a {account_a['description']} from {account_a['country']}"
        part2 = f"B: {account_b['name']}, a {account_b['description']} from {account_b['country']}"

        return f"Current Score = {score}\n{part1}\n{vs}\n{part2}"

    print(compose_question())
    return account_a, account_b


# 6
def validate_answer(a, b):
    answer = input("Who got more followers, A or B? Press E to quit : ").upper().strip()
    if a['follower_count'] > b['follower_count'] and answer == "A":
        print("Correct")
        return True

    elif answer == "E":
        return None

    else:
        print("Incorrect")
        return False


def update_score(score):
    score += 1
    return score


# 7
def end_game(name, database, score):
    database.loc[database.Player == name, "Score"] = score
    database.to_csv("player_database.csv", index=False)
    exit()
