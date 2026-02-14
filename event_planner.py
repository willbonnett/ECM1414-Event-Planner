'''
Main Python File for the running of the planner
'''
import time
from File_Handler import getData
from Brute_Force import bruteForce1D, bruteForce2D
from Dynamic_Algorithm import dymanic_algorithm
from Dynamic_Algorithm_2D import dynamic_algorithm_2d

def eventPlanner1Constraint(inputFile, constraint):
    activities, maxTime, maxBudget = getData(inputFile)

    print("====================================\n Event Planner - Results\n====================================")
    print(f"Input File = {inputFile}")
    print(f"Available Time: {maxTime}")
    print(f"Available Budget: {maxBudget}")

    print("\n--- Brute Force Algorithm ---")
    # Run Brute Force Algorithm
    bruteStart = time.time()
    bruteList,bruteEnjoy,bruteTime,bruteCost = bruteForce1D(activities,maxTime,maxBudget,constraint)
    bruteEnd = time.time()
    bruteExeTime = bruteEnd - bruteStart
    outputToConsole(bruteList,bruteEnjoy,bruteTime,bruteCost,bruteExeTime)

    print("\n--- Dynamic Algorithm ---")
    # Run Dynamic Programming Algorithm
    dynamStart = time.time()
    dynamList,dynamEnjoy,dynamTime,dynamCost = dymanic_algorithm(activities,maxTime,maxBudget,constraint)
    dynamEnd = time.time()
    dymanExeTime = dynamEnd - dynamStart
    outputToConsole(dynamList,dynamEnjoy,dynamTime,dynamCost,dymanExeTime)
    
    print("====================================")

def eventPlanner2Constraint(inputFile):
    activities, maxTime, maxBudget = getData(inputFile)

    print("====================================\n Event Planner - Results\n====================================")
    print(f"Input File = {inputFile}")
    print(f"Available Time: {maxTime}")
    print(f"Available Budget: {maxBudget}")

    print("\n--- Brute Force Algorithm ---")
    # Run Brute Force Algorithm
    bruteStart = time.time()
    bruteList,bruteEnjoy,bruteTime,bruteCost = bruteForce2D(activities,maxTime,maxBudget)
    bruteEnd = time.time()
    bruteExeTime = bruteEnd - bruteStart
    outputToConsole(bruteList,bruteEnjoy,bruteTime,bruteCost,bruteExeTime)

    print("\n--- Dynamic Algorithm ---")
    # Run Dynamic Programming Algorithm
    dynamStart = time.time()
    dynamList,dynamEnjoy,dynamTime,dynamCost = dynamic_algorithm_2d(activities,maxTime,maxBudget)
    dynamEnd = time.time()
    dymanExeTime = dynamEnd - dynamStart
    outputToConsole(dynamList,dynamEnjoy,dynamTime,dynamCost,dymanExeTime)
    
    print("====================================")


def outputToConsole(bestList, totalEnjoyment, totalTime, totalBudget, exeTime):
    # Formatting of output
    print("Selected Activities:")
    for activity in bestList:
        print(f" - {activity}")
    print(f"\nTotal Enjoyment: {totalEnjoyment}")
    print(f"Total Time Used: {totalTime} hours")
    print(f"Total Cost: £{totalBudget}")
    print(f"\nExecution Time: {exeTime} seconds")

if __name__ == "__main__":
    fileName = input("Enter Input File Name: ")
    constraint = input("Enter the Constraint (T,B or TB): ")
    if constraint == "TB":
        eventPlanner2Constraint(fileName)
    else:
        eventPlanner1Constraint(fileName,constraint)