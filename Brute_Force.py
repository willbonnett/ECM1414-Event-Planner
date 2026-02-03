from File_Handler import getData
from Power_Set_Calculator import getPowerSet
import time

activityList, maxTime, maxBudget = getData("input_10.txt")
powerSet = getPowerSet(activityList)

def isFeasible(activityList, maxTime, maxBudget):
    feasible = []
    for i in range(len(activityList)):
        totalTime, totalBudget = 0, 0
        for j in range(len(activityList[i])):
            totalTime += activityList[i][j][1]
            totalBudget += activityList[i][j][2]
        if totalTime <= maxTime and totalBudget <= maxBudget:
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

def brute_force():
    start_time = time.time()
    feasible = isFeasible(powerSet, maxTime, maxBudget)
    bestList, maxEnjoyment, totalTime, totalCost = bestActivities(feasible)
    end_time = time.time()

    print("--- Brute Force Algorithm ---")
    print("Selected Activities:")
    for i in range(len(bestList)):
        print(f"{bestList[i][0]} ({bestList[i][1]} hours, £{bestList[i][2]}, enjoyment {bestList[i][3]})")
    print("")
    print(f"Total Enjoyment: {maxEnjoyment}")
    print(f"Total Time Used: {totalTime} hours")
    print(f"Total Cost: £{totalCost}")
    print("")
    print(f"Exectution Time: {end_time - start_time:.4f} seconds")

brute_force()
