
def getData(file):
    file = open(file, "r")

    numActivities = int(file.readline())
    line2 = file.readline().split()

    maxTime = int(line2[0])
    maxBudget = int(line2[1])

    print("There are", numActivities, "activities.")
    print("The maximum available time is", maxTime)
    print("The maximum available budget is", maxBudget)
    print("")


    activityList = []

    for i in range(numActivities):
        nextLine = file.readline().split()
        for i in range(len(nextLine)):
            
            try:
                nextLine[i] = int(nextLine[i])
                
            except ValueError:
                continue
        
        activityList.append(nextLine)

    return activityList, maxTime, maxBudget


# example of how to call the function
# activityList, maxTime, maxBudget = getData("input_100.txt")
# activityList in the format [["Activity1", time required, cost, enjoyment value], [Activity2, ...], ...]



