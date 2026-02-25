from File_Handler import getData
from Power_Set_Calculator import getPowerSet

#Determines whether each activity in the powerset is possible with both constraints
def isFeasible2D(activityList, maxTime, maxBudget):
    feasible = []
    for i in range(len(activityList)):
        totalTime, totalBudget = 0, 0
        #Sum each constraint and checks that both values are below their maximum before appending
        for j in range(len(activityList[i])):
            totalTime += activityList[i][j][1]
            totalBudget += activityList[i][j][2]
        if totalTime <= maxTime and totalBudget <= maxBudget:
            feasible.append(activityList[i])
            
    return feasible

#Determines whether each activity in the powerset is possibles with one of the constraints
def isFeasible1D(activityList, maxTime, maxBudget, constraint):
    feasible = []
    #Use constraint to see whether time or budget is limiting
    if constraint == "T":
        constraintValue = maxTime
        valueIndex = 1
    elif constraint == "B":
        constraintValue = maxBudget
        valueIndex = 2

    #For each subset, check whether the total of the constraint is <= to the maximum value
    for i in range(len(activityList)):
        total = 0
        for j in range(len(activityList[i])):
            total += activityList[i][j][valueIndex]
        if total <= constraintValue:
            feasible.append(activityList[i])
    return feasible

#From the possible activities, find the list that has the largest enjoyment value
def bestActivities(feasible):
    maxEnjoyment = 0
    totalTime = 0
    totalCost = 0
    bestList = []
    #Compare the enjoyment for the current to the highest value found so far
    #Replace if the current value exceeds the highest value
    for i in range(len(feasible)):
        totalEnjoyment = 0
        for j in range(len(feasible[i])):
            totalEnjoyment += feasible[i][j][3]
        if maxEnjoyment < totalEnjoyment:
            maxEnjoyment = totalEnjoyment
            bestList = feasible[i]
    #After finding the best value, sum total time and total cost for the best list
    for i in range(len(bestList)):
        totalTime += bestList[i][1]
        totalCost += bestList[i][2]

    return bestList, maxEnjoyment, totalTime, totalCost


def bruteForce1D(activityList,maxTime,maxBudget,constraint):
    powerSet = getPowerSet(activityList)
    feasible = isFeasible1D(powerSet, maxTime, maxBudget,constraint)
    bestList, maxEnjoyment, totalTime, totalCost = bestActivities(feasible)

    return bestList, maxEnjoyment, totalTime, totalCost

def bruteForce2D(activityList,maxTime,maxBudget):
    powerSet = getPowerSet(activityList)
    feasible = isFeasible2D(powerSet, maxTime, maxBudget)
    bestList, maxEnjoyment, totalTime, totalCost = bestActivities(feasible)

    return bestList, maxEnjoyment, totalTime, totalCost
