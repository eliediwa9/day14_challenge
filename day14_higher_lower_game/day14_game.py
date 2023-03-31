# ************** Higher and Lower Game **********************
from functions import *
from data import data as questionary

# 1 Prompt player to enter name
load_logo()
player_name = user_info()

# 2 Save name of the player and his score
existing = existing_record(player_name)
if not existing:
    save_newrecord(player_name)

# 3 If player already exists, confirm that he want to continue with old score level
players_dtb = load_database(player_name, existing)
score = int(players_dtb.loc[players_dtb["Player"] == player_name, "Score"])

is_playing = True
while is_playing:

    # 4 clear screen and launch game
    clear_screen()

    # 5 Display question and prompt user to answer
    item_a, item_b = prompt_question(questionary, score)

    # 6 Update score if correct, not if wrong
    answer = validate_answer(item_a, item_b)
    if answer is True:
        score += 1

    elif answer is None:
        end_game(player_name, players_dtb, score)
