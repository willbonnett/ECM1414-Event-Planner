import math
# create a set of all possible subsets of activityList

def binaryAdd1(trueFalseList):
    '''
    Take a list of boolean values, adding one to it like it is binary.
    '''

    for i in range(len(trueFalseList)-1, 0, -1):
        
        # If we find a False, set it to True and the addition is complete
        if trueFalseList[i] == False:
            
            trueFalseList[i] = True
            break

        # If we find a True, set it to false and keep going
        # Like carrying the one in binary addition
        elif trueFalseList[i] == True:
            trueFalseList[i] = False

    return trueFalseList


def getPowerSet(activityList):
    '''
    Uses a list of boolean values as a mask to create every possible subset of activityList
    '''
    
    # create a list consisting only of false values, and initialise the powerset as an empty list
    powerSetMask = [False for x in range(len(activityList))]
    powerSet = []

    for i in range(2**len(activityList)):
        currentList = []

        # combine the activityList with the boolean mask to create a subset
        for i in range(len(activityList)):
            if powerSetMask[i] == True:
                currentList.append(activityList[i])

        # append the subset to the power set list
        powerSet.append(currentList)

        # perform a binary add 1 to the power set list, creating a new mask
        powerSetMask = binaryAdd1(powerSetMask)


    return powerSet


# call powerSet = getPowerSet(activityList)
# will return a list of every possible combination of activities (including an empty list)
