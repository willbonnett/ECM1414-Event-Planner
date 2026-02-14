from File_Handler import getData
import numpy as np

#print(activities)



def dymanic_algorithm(activities, maxTime, maxBudget,constraint, debug = False):
    '''
    The function will create a one dimesional array of the length of the max_constraint_value setting values to zero initially.
    Then the program will iterate through the available activties and backtrack through the array working out the max enjoyment
    values that can be achieved with the currently selected activity.

    If an activity gets chosen for a larger enjoyment, then in a parallel array, the path to get the current max enjoyment for 
    that time values is stored. The new largest enjoyment path is just the path of the time before the current activity with
    the new activity appended on.

    Parameters:
    activities - list of activities
    constraint - either "T" or "B" depicting time or budget
    constraint_value - the max value of the chosen constraint
    debug - If you want the steps the algorithm takes printed
    '''


    # Check for the selected constraint
    if constraint == "T":
        constraint_value = maxTime
        valueIndex = 0
    elif constraint == "B":
        constraint_value = maxBudget
        valueIndex = 1

    # create arrays of length constraint_value
    maxEnjoyment = np.zeros(constraint_value+1) # holds max possible enjoyment in given time
    path = [[] for _ in range(constraint_value+1)] # holds the last activity that maxmises enjoyment

    # Iterate through the activities 
    for activity, time, budget, enjoyment in activities:

        values = [time,budget]
        if debug: print(f"\n--- New Activity: {activity} T/B value: {values[valueIndex]} Enjoyment: {enjoyment} ---")
        
        # Backtrack through the maxEnjoyment,
        for i in range(len(maxEnjoyment)-1,0,-1):
            if (i- values[valueIndex]) < 0:
                # If the activity cannot be completed before this time/budget
                continue
            elif maxEnjoyment[i - values[valueIndex]] + enjoyment >= maxEnjoyment[i]:
                # current activity results in higher enjoyment
                # Update new maxEnjoyment
                maxEnjoyment[i] = maxEnjoyment[i - values[valueIndex]] + enjoyment
                if debug: print(f"higher maxEnjoyment found, is now {maxEnjoyment[i]} for constrain value:{i}")

                # Update the path that got to the highest
                path[i] = path[i - values[valueIndex]] + [[activity, values, enjoyment]]
                if debug: print(f"previous path is {path[i - values[valueIndex]]}")


    # Return the needed values
    i = np.argmax(maxEnjoyment)
    timeUsed = 0
    budgetUsed = 0
    for activity in path[i]:
        timeUsed += activity[1][0]
        budgetUsed += activity[1][1]

    return path[i], maxEnjoyment[i], timeUsed, budgetUsed