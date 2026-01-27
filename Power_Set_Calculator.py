import math
from File_Handler import getData

activityList, maxTime, maxBudget = getData("input_100.txt")

# create a set of all possible subsets of activityList

def binaryAdd1(trueFalseList):
    for i in range(len(trueFalseList)-1, 0, -1):
        
        if trueFalseList[i] == False:
            
            trueFalseList[i] = True
            break

        elif trueFalseList[i] == True:
            trueFalseList[i] = False

    return trueFalseList
        

def getPowerSet(activityList):
    powerSetMask = [False for x in range(len(activityList))]

    powerSet = []

    for i in range(2**len(activityList)):
        currentList = []

        for i in range(len(activityList)):
            if powerSetMask[i] == True:
                currentList.append(activityList[i])

        powerSet.append(currentList)

        powerSetMask = binaryAdd1(powerSetMask)


    return powerSet


# call powerSet = getPowerSet(activityList)
# will return a list of every possible combination of activities (including an empty list)
