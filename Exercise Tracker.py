import pandas as pd

"""Plan
Part 1:  The user can log how many reps/km they did. IF they don't wish to log the day then the result given will be 0 for the exercises that day.
after 3 days have been logged the program will stop and congratulate the
user on doing their weeks worth of exercise.

Part 2: the week logging can be run again and again all while updating a user profile will gives awards depending on if the user passed goals or not. """

def pressup_value():
    """get quantity of pressups achieved in a day"""
    while True:
        try:
            pressups_value = int(input("\nHow many pressups have you done today? "))
        except ValueError:
            print("\nNo value entered, enter 0 if no pressups done")
            continue
        else:
            return pressups_value

def run_value():
    """get run distance achieved in a day"""
    while True:
        try:
            runs_value = int(input("How many Km have you run today? "))
        except ValueError:
            print("\nNo value entered, enter 0 if no Km run")
            continue
        else:
            return runs_value

def situp_value():
    """get quantity of situps achieved in a day"""
    while True:
        try:
            situps_value = int(input("How many situps have you done today? "))
        except ValueError:
            print("\nNo value entered, enter 0 if no situps done")
            continue
        else:
            return situps_value

def squat_value():
    """get quantity of Squats achieved in a day"""
    while True:
        try:
            squats_value = int(input("How many squats have you done today? "))
        except ValueError:
            print("\nNo value entered, enter 0 if no squats done")
            continue
        else:
            return squats_value
            


def log_numbers(pressups_value, runs_value, situps_value, squats_value):
    """Find out if they would like to log the exercise list, if they say no, the results for the exercises will be 0"""
    log = input("\nDo you wish to log your workout (y/n)? ").lower()    
    if log == 'y': 
        #log to the exercise list
        pressups.append(pressups_value)       
        runs.append(runs_value)
        situps.append(situps_value)
        squats.append(squats_value)

        #log to the prize list
        log_pressups.append(pressups_value)       
        log_runs.append(runs_value)
        log_situps.append(situps_value)
        log_squats.append(squats_value)
        
        return pressups_value, runs_value, situps_value, squats_value
    else:
        pressups.append(0)       
        runs.append(0)
        situps.append(0)
        squats.append(0)
        log_pressups.append(0)       
        log_runs.append(0)
        log_situps.append(0)
        log_squats.append(0)
        return pressups_value, runs_value, situps_value, squats_value
    
def ex_log(pressups, runs, situps, squats):
    """append values from list to dictionary """
    exercise['Pressups'].append(pressups[-1])
    exercise['Runs'].append(runs[-1])
    exercise['Situps'].append(situps[-1])
    exercise['Squats'].append(squats[-1])


def dict_prize():
    #log prizes for pressups
    if log_pressups[-1] >= 20:
        prize['Pressups Prize'].append("Gold")
    elif log_pressups[-1] >= 15 and log_pressups[-1] < 20:
        prize['Pressups _Prize'].append("Silver")
    elif log_pressups[-1] >= 5 and log_pressups[-1] < 15:
        prize['Pressups Prize'].append("Bronze")
    else:
        prize['Pressups Prize'].append("Fail")

    #log prizes for running
    if log_runs[-1] >= 10:
        prize['Running Prize'].append("Gold")
    elif log_runs[-1] >= 6 and log_runs[-1] < 10:
        prize['Running Prize'].append("Silver")
    elif log_runs[-1] >= 2 and log_runs[-1] < 6:
        prize['Running Prize'].append("Bronze")
    else:
        prize['Running Prize'].append("Fail")

    #log prizes for situps
    if log_situps[-1] >= 20:
        prize['Situps Prize'].append("Gold")
    elif log_situps[-1] >= 15 and log_situps[-1] < 20:
        prize['Situps Prize'].append("Silver")
    elif log_situps[-1] >= 5 and log_situps[-1] < 15:
        prize['Situps Prize'].append("Bronze")
    else:
        prize['Situps Prize'].append("Fail")
    

    #log prizes for squats
    if log_squats[-1] >= 20:
        prize['Squats Prize'].append("Gold")
    elif log_squats[-1] >= 15 and log_squats[-1] < 20:
        prize['Squats Prize'].append("Silver")
    elif log_squats[-1] >= 5 and log_squats[-1] < 15:
        prize['Squats Prize'].append("Bronze")
    else:
        prize['Squats Prize'].append("Fail")

#Give prizes according to exercises achieved
def prizeGiven():
    """gives a value to the prize lists, after 7 days of exercise, a summary will be given of the prizes achieved in the week."""
    if len(prize['Pressups Prize']) == 7 or len(prize['Pressups Prize']) == 14 or len(prize['Pressups Prize']) == 21 or len(prize['Pressups Prize']) == 28:
        for value in prize['Pressups Prize']:
            if value == "Gold":
                gold.append(1)
            elif value == "Silver":
                silver.append(1)
            elif value == "Bronze":
                bronze.append(1)
            else:
                fail.append(1)

        for value in prize['Running Prize']:
            if value == "Gold":
                gold.append(1)
            elif value == "Silver":
                silver.append(1)
            elif value == "Bronze":
                bronze.append(1)
            else:
                fail.append(1)

        for value in prize['Situps Prize']:
            if value == "Gold":
                gold.append(1)
            elif value == "Silver":
                silver.append(1)
            elif value == "Bronze":
                bronze.append(1)
            else:
                fail.append(1)

        for value in prize['Squats Prize']:
            if value == "Gold":
                gold.append(1)
            elif value == "Silver":
                silver.append(1)
            elif value == "Bronze":
                bronze.append(1)
            else:
                fail.append(1)

        goldSum = sum(gold)
        silverSum = sum(silver)
        bronzeSum = sum (bronze)
        failSum = sum(fail)

        print("\nSummary of prizes for the week")
        print("This week you have earned " + str(goldSum) + " Golds, " + str(silverSum) + " Silvers, " + str(bronzeSum) + " Bronzes, and " + str(failSum) + " Fails.")
        

#lists for the exercise table   
pressups = []
runs = []
situps = []
squats = []

#lists for the prize table
log_pressups = []
log_runs = []
log_situps = []
log_squats = []

#goku = []
gold = []
silver = []
bronze = []
fail = []

exercise = {'Pressups': [], 'Runs': [], 'Situps': [], 'Squats': []}
prize = {'Pressups Prize':[], 'Running Prize':[], 'Situps Prize':[], 'Squats Prize':[]}

P_prize_total = []
repeat = []

#main code
"""intro to the tracker"""
print("Welcome to the fitness tracker")
print("Follow your progress of your exercises for the month with weekly summaries.\n")


training = True
while training:
    print("\nPressups levels: Gold = 20+    Silver = 15-19    Bronze = 5-14   Fail =  < 5")
    print("Runs (Km) levels: Gold = 10+    Silver = 6-9    Bronze = 2-5   Fail =  < 2")
    print("Situps levels: Gold = 20+    Silver = 15-19    Bronze = 5-14   Fail =  < 5")
    print("Squats levels: Gold = 20+    Silver = 15-19    Bronze = 5-14   Fail =  < 5")
    print("\n\tIF YOU DON'T LOG YOU WORKOUT, VALUES WILL BE 0 FOR THE DAY\n")

    """collect values for the days exercises"""
    press = pressup_value()
    run = run_value()
    situp = situp_value()
    squat = squat_value()

    """log the numbers to the lists"""
    log = log_numbers(press, run, situp, squat)   
    update_dict = ex_log(pressups, runs, situps, squats)
    
    """log the prizes for each exercise"""
    dict_prize()

    """put values into the table"""  
    ex_table = pd.DataFrame(exercise)
    prize_table = pd.DataFrame(prize)

    """print out the tables"""
    print("\n------------------------------------------------------------------")
    print(ex_table)
    print("\n\t-------------------------------------------------\n")
    print(prize_table)
    print("--------------------------------------------------------------------")
    prizeGiven()

    #set conditions for continuing or closing the program
    if len(prize['Pressups Prize']) == 7 or len(prize['Pressups Prize']) == 14 or len(prize['Pressups Prize']) == 21 or len(prize['Pressups Prize']) == 28:
        again = input("\nDo you wish to log exercises for another week?  (y/n) (selecting no will end the program): \n").lower()
        if again != "y":
            repeat.append(1)
            if repeat[0] == 1 and len(prize["Pressups Prize"]) == 7:     
                print("\nYou have completed a weeks training, good job.")
                break
            elif repeat[0] == 1 and len(prize["Pressups Prize"]) == 14:     
                print("\nYou have completed 2 weeks training, good job.")
                break          
            elif repeat[0] == 1 and len(prize["Pressups Prize"]) == 21:  
                print("\nYou have completed 3 weeks training, good job.")
                break
            elif repeat[0] == 1 and len(prize["Pressups Prize"]) == 28:  
                print("\nYou have completed 4 weeks training, good job.")
                ended = input("\nPress Enter to end the program")
                break
    if len(prize["Pressups Prize"]) == 28:
        print("\nYou have completed a months training, Relax!")
        ended = input("\nPress Enter to end the program")
        break
                

    

    






