import csv
import PySimpleGUI as sq

def average_amp_scoring(data, team, last_num_of_games, sep):
    results = 0
    count = 0
    r_list = []
    for row in data:
        r_list.insert(0, row)
    for item in r_list:
        if item["team"] == str(team):
            count += 1
            if sep != 2:
                for i in range(len(item["auto scoring"])):
                    if item["auto scoring"][i] == "a":
                        if item["auto scoring"][i + 1] == "s":
                            results += 1
            if sep != 1:
                for b in range(len(item["teleop scoring"])):
                    if item["teleop scoring"][b] == "a":
                        if item["teleop scoring"][b + 1] == "s":
                            results += 1
            if count == last_num_of_games:
                return str(team) + " scored speaker " + str(results / count) + " times per match in the last " \
                       + str(last_num_of_games) + " matches.\n"
    if count == 0:
        return str(team) + " did not attend this event.\n"
    return str(team) + " scores amp " + str(results / count) + " times per match on average.\n"


def average_speaker_scoring(data, team, last_num_of_games, sep):
    results = 0
    count = 0
    r_list = []
    for row in data:
        r_list.insert(0, row)
    for item in r_list:
        if item["team"] == str(team):
            count += 1
            if sep != 2:
                for i in range(len(item["auto scoring"])):
                    if item["auto scoring"][i] == "s":
                        if item["auto scoring"][i + 1] == "s":
                            results += 1
            if sep != 1:
                for b in range(len(item["teleop scoring"])):
                    if item["teleop scoring"][b] == "s":
                        if item["teleop scoring"][b + 1] == "s" or item["teleop scoring"][b + 1] == "a":
                            results += 1
            if count == last_num_of_games:
                return str(team) + " scored speaker " + str(results / count) + " times per match in the last " \
                       + str(last_num_of_games) + " matches.\n"
    if count == 0:
        return str(team) + " did not attend this event.\n"
    return str(team) + " scores speaker " + str(results / count) + " times per match on average.\n"


def amp_percentage(data, team, last_num_of_games, sep):
    made = 0
    total = 0
    count = 0
    r_list = []
    for row in data:
        r_list.insert(0, row)
    for item in r_list:
        if item["team"] == str(team):
            count += 1
            if sep != 2:
                for i in range(len(item["auto scoring"])):
                    if item["auto scoring"][i] == "a":
                        if item["auto scoring"][i + 1] == "s":
                            made += 1
                            total += 1
                        elif item["auto scoring"][i + 1] == "m":
                            total += 1
            if sep != 1:
                for b in range(len(item["teleop scoring"])):
                    if item["teleop scoring"][b] == "a":
                        if item["teleop scoring"][b + 1] == "s":
                            made += 1
                            total += 1
                        elif item["teleop scoring"][b + 1] == "m":
                            total += 1
            if count == last_num_of_games:
                if total == 0:
                    return str(team) + " did not attempt to score amp during these matches."
                return str(team) + " made " + str(
                    (made / total) * 100) + "% of their amp shots in the last " + str(
                    last_num_of_games) + " matches\n"
    if total == 0:
        return str(team) + " did not attempt to score amp.\n"
    if count == 0:
        return str(team) + " did not attend this event.\n"
    return str(team) + " made " + str((made / total) * 100) + "% of their amp shots.\n"


def speaker_percentage(data, team, last_num_of_games, sep):
    made = 0
    total = 0
    count = 0
    r_list = []
    for row in data:
        r_list.insert(0, row)
    for item in r_list:
        if item["team"] == str(team):
            count += 1
            if sep != 2:
                for i in range(len(item["auto scoring"])):
                    if item["auto scoring"][i] == "s":
                        if item["auto scoring"][i + 1] == "s":
                            made += 1
                            total += 1
                        elif item["auto scoring"][i + 1] == "m":
                            total += 1
            if sep != 1:
                for b in range(len(item["teleop scoring"])):
                    if item["teleop scoring"][b] == "s":
                        if item["teleop scoring"][b + 1] == "s" or item["auto scoring"][b + 1] == "a":
                            made += 1
                            total += 1
                        elif item["teleop scoring"][b + 1] == "m":
                            total += 1
            if count == last_num_of_games:
                if total == 0:
                    return str(team) + " did not attempt to score speaker during these matches."
                return str(team) + " made " + str(
                    (made / total) * 100) + "% of their speaker shots in the last " + str(
                    last_num_of_games) + " matches\n"

    if total == 0:
        return str(team) + " did not attempt to score speaker.\n"
    if count == 0:
        return str(team) + " did not attend this event.\n"
    return str(team) + " made " + str((made / total) * 100) + "% of their speaker shots.\n"


def average_auto(data, team, last_num_of_games):
    points = 0
    count = 0
    r_list = []
    for row in data:
        r_list.insert(0, row)
    for item in r_list:
        if item["team"] == str(team):
            count += 1
            for i in range(len(item["auto scoring"])):
                if item["auto scoring"][i] == "s" and item["auto scoring"][i + 1] == "s":
                    points += 5
                elif item["auto scoring"][i] == "a" and item["auto scoring"][i + 1] == "s":
                    points += 2
            if item["leave"] == "true":
                points += 2
            if count == last_num_of_games:
                return str(team) + " scored " + str(points / count) + " points on average during auto\n"
    if count == 0:
        return str(team) + " did not attend this event.\n"
    return str(team) + " scored " + str(points / count) + " points on average during auto\n"


def average_endgame(data, team, last_num_of_games):
    points = 0
    count = 0
    r_list = []
    for row in data:
        r_list.insert(0, row)
    for item in r_list:
        if item["team"] == str(team):
            count += 1
            for i in range(len(item["teleop scoring"])):
                if item["teleop scoring"][i] == "t" and item["teleop scoring"][i + 1] == "s":
                    points += 5
            if item["stage level"] == '2':
                if item["spotlight"] == "true":
                    points += 4
                else:
                    points += 3
            elif item["stage level"] == '1':
                points += 1
            elif item["stage level"] == '3':
                points += 5
            if count == last_num_of_games:
                return str(team) + " scored " + str(points / count) + " stage points on average\n"
    if count == 0:
        return str(team) + " did not attend this event.\n"
    return str(team) + " scored " + str(points / count) + " stage points on average\n"


file_path = input("Please copy and paste the exact file path of the CSV file. ")
data_list = []
with open(file_path) as file:
    csv_reader = csv.DictReader(file)

    for r in csv_reader:
        data_list.append(r)

    while True:
        choice = input("Enter a number, or type 'done' to end the program.\n"
                       "1. Average Amp Scoring\n"
                       "2. Average Speaker Scoring\n"
                       "3. Amp Percentage\n"
                       "4. Speaker Percentage\n"
                       "5. Average Auto Score\n"
                       "6. Average Endgame Score\n")
        if choice == "done":
            break
        elif choice in ["1", "2", "3", "4"]:
            data_filter = int(input("\nChoose one of the following:\n"
                                    "1. Find only autonomous data\n"
                                    "2. Find only teleop data\n"
                                    "3. Find combined data\n"))
            if data_filter == 1:
                print("AUTONOMOUS")
            elif data_filter == 2:
                print("TELEOP")
            else:
                print("COMBINED")

            team_num = int(input("Enter a team number. "))
            rounds = int(input("Enter the number of rounds you want to consider, or enter 0 to consider all rounds. "))
            if choice == "1":
                print("\n" + average_amp_scoring(data_list, team_num, rounds, data_filter))
            elif choice == "2":
                print("\n" + average_speaker_scoring(data_list, team_num, rounds, data_filter))
            elif choice == "3":
                print("\n" + amp_percentage(data_list, team_num, rounds, data_filter))
            elif choice == "4":
                print("\n" + speaker_percentage(data_list, team_num, rounds, data_filter))
        elif choice in ["5", "6"]:
            team_num = int(input("Enter a team number. "))
            rounds = int(input("Enter the number of rounds you want to consider, or enter 0 to consider all rounds. "))
            if choice == "5":
                print("\n" + average_auto(data_list, team_num, rounds))
            else:
                print("\n" + average_endgame(data_list, team_num, rounds))
        else:
            print("Please choose a valid choice.\n")
            continue

# All the stuff inside your window.
layout = [  [sg.Text("What's your name?")],
            [sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Hello Example', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    print('Hello', values[0], '!')

window.close()