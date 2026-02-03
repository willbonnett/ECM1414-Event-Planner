import numpy as np
from File_Handler import getData
import time


activities, max_time, max_budget = getData("input_10.txt")


def dynamic_algorithm_2d(activities, max_t, max_b):
    # maximum enjoyment possible for that time and budget
    dp = np.zeros((max_t + 1, max_b + 1))
    
    
    # store the list of activity names 
    path = [[[] for _ in range(max_b + 1)] for _ in range(max_t + 1)]

    start_time = time.time()

    for name, t_cost, b_cost, enjoyment in activities:
        # We iterate backwards through time and budget 
        for t in range(max_t, t_cost - 1, -1):
            for b in range(max_b, b_cost - 1, -1):
                
                # Check if adding this activity is better than what we had before
                new_enjoyment = dp[t - t_cost][b - b_cost] + enjoyment
                
                if new_enjoyment > dp[t][b]:
                    dp[t][b] = new_enjoyment
                    # taking the previous best path and adding this activity
                    path[t][b] = path[t - t_cost][b - b_cost] + [name]

    end_time = time.time()

    # where the maximum enjoyment is located 
    best_t, best_b = np.unravel_index(np.argmax(dp), dp.shape)
    
    
    print(f"- Results -")
    print(f"Selected Activities: {', '.join(path[best_t][best_b])}")
    print(f"Total Enjoyment: {dp[best_t][best_b]}")
    print(f"Time Used: {best_t} / {max_t}")
    print(f"Budget Used: {best_b} / {max_b}")
    print(f"Execution Time: {end_time - start_time:.4f} seconds")

dynamic_algorithm_2d(activities, max_time, max_budget)
