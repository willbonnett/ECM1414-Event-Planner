from File_Handler import getData
import numpy as np


activities, max_time, max_budget = getData("input_10.txt")
#print(activities)



def dymanic_algorithm(activities, constraint, constraint_value, debug = False):
    '''
    The function will create a one dimesional array of the length of the max_constraint_value setting values to zero initially.
    Then the program will iterate through the available activties and backtrack through the array working out the max enjoyment
    values that can be achieved with the currently selected activity.

    If an activity gets chosen for a larger enjoyment, then in a parallel array, the activity is stored under the index of where it
    provides the most enjoyment as a way to once all activities have been iterated through return the path.

    Parameters:
    activities - list of activities
    constraint - either "T" or "B" depicting time or budget
    constraint_value - the max value of the chosen constraint
    debug - If you want the steps the algorithm takes printed
    '''


    # Check for the selected constraint
    if constraint == "T":
        valueIndex = 0
    elif constraint == "D":
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
                path[i] = path[i - values[valueIndex]] + [[activity, values[valueIndex], enjoyment]]
                if debug: print(f"previous path is {path[i - values[valueIndex]]}")


    # Backtrack through the array selecting the last chosen activities
    i = np.argmax(maxEnjoyment)
    print("\nSelected Most Efficient path is :" + str(path[i]))
    print("Time / Budget Used:" + str(i))
    print("Total Enjoyment:" + str(maxEnjoyment[i]))


dymanic_algorithm(activities,"T",max_time,True)