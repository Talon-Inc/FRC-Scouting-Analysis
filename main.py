import csv
import PySimpleGUI as sg

def average_amp_scoring(data, team, last_num_of_games, sep):
    results = 0
    count = 0
    for item in data[team]:
        count += 1
        if sep != 2:
            for a in item['auto scoring']:
                if a == 'as':
                    results += 1
        if sep != 1:
            for t in item['teleop scoring']:
                if t == 'as':
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
    for item in data[team]:
        count += 1
        if sep != 2:
            for a in item['auto scoring']:
                if a == 'ss':
                    results += 1
        if sep != 1:
            for t in item['teleop scoring']:
                if t == 'ss':
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
    for item in data[team]:
        count += 1
        if sep != 2:
            for a in item['auto scoring']:
                if a == 'as':
                    made += 1
                total += 1
        if sep != 1:
            for t in item['teleop scoring']:
                if t == 'as':
                    made += 1
                total += 1
        if count == last_num_of_games:
            if total == 0:
                return str(team) + " did not attempt to score speaker during these matches."
            return str(team) + " made " + str(
                (made / total) * 100) + "% of their speaker shots in the last " + str(
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
    for item in data[team]:
        count += 1
        if sep != 2:
            for a in item['auto scoring']:
                if a == 'ss':
                    made += 1
                total += 1
        if sep != 1:
            for t in item['teleop scoring']:
                if t == 'ss' or t == 'sa':
                    made += 1
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
    for row in data[team]:
        count += 1
        for p in row["auto scoring"]:
            if p == "ss":
                points += 5 # score speaker
            elif p == "as":
                points += 2 # score amp
        if row["leave"] == "true":
            points += 2 # score leaving
        if count == last_num_of_games:
            return str(team) + " scored " + str(points / count) + " points on average during auto\n"
    if count == 0:
        return str(team) + " did not attend this event.\n"
    return str(team) + " scored " + str(points / count) + " points on average during auto\n"

def average_endgame(data, team, last_num_of_games):
    points = 0
    count = 0
    for item in data[team]:
        count += 1
        for i in item['teleop scoring']:
            if i == 'ts':
                points += 5
        if item['stage level'] == '2':
            if item['spotlight'] == 'true':
                points += 4
            else:
                points += 3
        elif item['stage level'] == '1':
            points += 1
        elif item['stage level'] == '3':
            points += 5
        if count == last_num_of_games:
            return str(team) + " scored " + str(points / count) + " stage points on average\n"
    if count == 0:
        return str(team) + " did not attend this event.\n"
    return str(team) + " scored " + str(points / count) + " stage points on average\n"

def add_to_master_dict(master_dict, data):
    team = data['team']
    team_data = data.copy()
    team_data.pop('')
    team_data.pop('team')
    team_data.pop('scouter')
    team_data.pop('timestamp')
    # convert auto and teleop scores to lists
    auto_list = team_data['auto scoring'][1:-1].split(",")
    team_data['auto scoring'] = [s.strip() for s in auto_list]
    teleop_list = team_data['teleop scoring'][1:-1].split(",")
    team_data['teleop scoring'] = [s.strip() for s in teleop_list]

    # if team doesn't exist, create team
    if team not in master_dict:
        master_dict[team] = []
    # add data to team
    master_dict[team].append(team_data)

# file_path = input("Please copy and paste the exact file path of the CSV file: ")
file_path = "C:\\Users\\tiger\\Downloads\\tpw-scouting-2024txpla.csv"
data_dict = {}
data_list = []
exclude = []
with open(file_path) as file:
    csv_reader = csv.DictReader(file)
    # print(csv_reader.restkey["4641"])
    for data in csv_reader:
        add_to_master_dict(data_dict, data)
    print(data_dict['148'][-1])

    while True:
        choice = input("Enter a number, or type 'done' to end the program.\n"
                       "1. Average Amp Scoring\n"
                       "2. Average Speaker Scoring\n"
                       "3. Amp Percentage\n"
                       "4. Speaker Percentage\n"
                       "5. Average Auto Score\n"
                       "6. Average Endgame Score\n"
                       "Enter: ")
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
