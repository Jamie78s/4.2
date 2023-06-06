import time
import random
import sys

ver = '1.0.0'
# Version format
# a.b.c
# a = major version
# b = minor version
# c = patch version

# Point system
# Teams
# 1st place = 3 points
# 2nd place = 2 points
# 3rd place = 1 point
# 4th place = 0 points

# Individuals
# 1st place = 5
# 2nd place = 4
# 3rd place = 3
# 4th place = 2
# 5th place = 1

def howUse():
    print('How to use:')
    print("During a decision you can answer with a number or the term it's asking you to select")
    print('In a yes or no question you can answer with a number, yes/no or y/n')
    print('Multiple choice answers are case-insensitive however during free type questions they are case-sensitive')
def getMode():
    mode = False
    while  mode == False:
        mode = input('Are you playing with "Teams" or "Individuals"? ').lower()

        if mode == 'teams' or mode == 't':
            mode = 'team'
        elif mode == 'individuals' or mode == 'i':
            mode = 'individual'
        else:
            print("Thats not valid, please try again.")
            mode = False
            time.sleep(0.2)

        return mode
    
def createTeams(mode):
    print(f'You are creating a {mode}, please leave {mode} name blank to stop')
    teams = [{'name':'','points':999}]
    if mode == "team":
        j = 4
    else:
        j = 20
    for i in range (0,j):
        name = input(f"Choose the name of the {mode} {i+1}\n")
        if name == "":
            break
        teams.append({"name":name,"points":0})
        return teams
    
def createEvents():
    print("You are now applying for events. To stop crating events, leave an event name blank")
    events = [{'name':'','complete':''}]
    i = 0
    while True:
        i += 1
        eventName = input(f"Enter the name for your event {i}\n")
        if eventName == "":
            break
        events.append({"name":eventName,"complete":False})
        return events

def completeEvent(events,teams):
    eName = events['name']
    events['complete'] = True
    print(f"prepare to take the scores for each position.")
    positions = []
    j = len(teams)
    print(f"{mode}s")
    for i in range(j-1):
        print(teams[i+1]["name"])
    print(f"positions for {eName}")
    for i in range (0,j-1):
        x = i+1
        x = str(x)
        if x[-1] == "1":
            x = x + "st"
        elif x[-1] == "2":
            x = x + "nd"
        elif x[-1] == "3":
            x = x + "rd"
        else:
            x = x + "th"
        while True:
            a = input(f"Enter the name of the player who achieved {x}\n")
            a = next((i for i, item in enumerate(teams) if item["name"] == a), False)
            if a !=False:
                positions.append(a)
                break
            else:
                print("That team or player does not exist")

    if j-1 >= 15:
        awardTo = 5
    elif j-1 >= 10:
        awardTo = 4
    elif j-1 >= 5:
        awardTo = 3
    elif j-1 >= 3:
        awardTo = 2
    elif j-1 >= 1:
        awardTo = 1
    for i in range(j-1):
        if awardTo == 0:
            break
        else:
            teams[positions[i]]['points'] += awardTo
            awardTo -= 1
    print("current points awarded:")
    for i in range(j-1):
        print(f"{teams[i+1]['name']} - {teams[i+1]['points']}")

players = 0
teams = 0
awardTo = 0 #Also acts as the maximum prize for First Place. -1 for every place below
if players >= 15:
    awardTo = 5
elif players >= 10:
    awardTo = 4
elif players >= 5:
    awardTo
elif players >= 3:
    awardTo = 2
elif players >= 1:
    awardTo = 1

# TESTING SPACE SRT #
# team =  [{'name':'test','points':0}]
# print(team)
# TESTING SPACE END #

print("Welcome to the Judgemental System")
print("Version "+ver)
time.sleep(0.2)
howUse()
time.sleep(1)
mode = getMode()
#print(mode)
teams = createTeams(mode)
#print(teams)
events = createEvents()
#print(events)
while True:
    while True:
        selection = input("Please select an event you would like to compete in\n")
        try:
            s = int(selection)
            if events[s]['complete'] == False:
                break
            else:
                print("This event is already completed")
                continue
        except ValueError:
            s = next((i for i, item in enumerate(events)if item["name"].lower() == selection.lower()), False)
            if s == False:
                print("Invalid entry")
                continue
            if events[s]['complete'] == False:
                break
            else:
                print("This event is already completed")
                continue
            break
        except AttributeError:
            print("Invalid Entry")
        except IndexError:
            print("Invalid Entry")
            completeEvent(events[s],teams)
            if next((i for i, item in enumerate(events) if item["complete"] == False), False) == False:
                #print(teams)
                final = sorted(teams, key=lambda d: d['points'], reverse=True)
                print("Final Rankings: ")
                for i in range(len(final)):
                    if i == 0:
                        continue
                    x = i
                    x = str(x)
                    if x[-1] == "1":
                        x = x + "st"
                    elif x[-1] == "2":
                        x = x + "nd"
                    elif x[-1] == "3":
                        x = x + "rd"
                    else:
                        x = x + "th"

                        print(f"{x} - {final[i]['name']} - {final[i]['points']} points")

                        print("All events have now been completed. This program will now close")
                        time.sleep(5)
                        break
                    sys.exit()