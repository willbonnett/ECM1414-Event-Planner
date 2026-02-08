
def getData(file, debug = False):
    file = open(file, "r")

    # the first line of the file holds only the number of activities
    numActivities = int(file.readline())

    # split the second line into a list of items seperated by spaces (should be 2 items)
    line2 = file.readline().split()

    # the first number in the second line is the time constraint, second is budget constraint
    maxTime = int(line2[0])
    maxBudget = int(line2[1])

    if debug:
        print("There are", numActivities, "activities.")
        print("The maximum available time is", maxTime)
        print("The maximum available budget is", maxBudget)
        print("")

    # create an empty list to hold the activities
    activityList = []

    for i in range(numActivities):

        # split each line into a list of items
        nextLine = file.readline().split()
        for i in range(len(nextLine)):
            
            # if a number, convert to integer
            try:
                nextLine[i] = int(nextLine[i])
                
            except ValueError:
                continue
        
        # append a list containing [activityName, time, money] to activityList
        activityList.append(nextLine)

    file.close()
    return activityList, maxTime, maxBudget


# example of how to call the function
# activityList, maxTime, maxBudget = getData("input_100.txt")
# activityList in the format [["Activity1", time required, cost, enjoyment value], [Activity2, ...], ...]



