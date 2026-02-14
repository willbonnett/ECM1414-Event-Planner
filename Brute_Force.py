from File_Handler import getData
from Power_Set_Calculator import getPowerSet


def isFeasible2D(activityList, maxTime, maxBudget):
    feasible = []
    for i in range(len(activityList)):
        totalTime, totalBudget = 0, 0
        for j in range(len(activityList[i])):
            totalTime += activityList[i][j][1]
            totalBudget += activityList[i][j][2]
        if totalTime <= maxTime and totalBudget <= maxBudget:
            feasible.append(activityList[i])
            
    return feasible

def isFeasible1D(activityList, maxTime, maxBudget, constraint):
    feasible = []
    if constraint == "T":
        constraintValue = maxTime
        valueIndex = 1
    elif constraint == "B":
        constraintValue = maxBudget
        valueIndex = 2

    for i in range(len(activityList)):
        total = 0
        for j in range(len(activityList[i])):
            total += activityList[i][j][valueIndex]
        if total <= constraintValue:
            feasible.append(activityList[i])
    return feasible

def bestActivities(feasible):
    maxEnjoyment = 0
    totalTime = 0
    totalCost = 0
    bestList = []
    for i in range(len(feasible)):
        totalEnjoyment = 0
        for j in range(len(feasible[i])):
            totalEnjoyment += feasible[i][j][3]
        if maxEnjoyment < totalEnjoyment:
            maxEnjoyment = totalEnjoyment
            bestList = feasible[i]
    
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
