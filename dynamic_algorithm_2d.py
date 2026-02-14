import numpy as np

def dynamic_algorithm_2d(activities, max_t, max_b):
    # maximum enjoyment possible for that time and budget
    dp = np.zeros((max_t + 1, max_b + 1))
    
    
    # store the list of activity names 
    path = [[[] for _ in range(max_b + 1)] for _ in range(max_t + 1)]

    for name, t_cost, b_cost, enjoyment in activities:
        # We iterate backwards through time and budget 
        for t in range(max_t, t_cost - 1, -1):
            for b in range(max_b, b_cost - 1, -1):
                
                # Check if adding this activity is better than what we had before
                new_enjoyment = dp[t - t_cost][b - b_cost] + enjoyment
                
                if new_enjoyment > dp[t][b]:
                    dp[t][b] = new_enjoyment
                    # taking the previous best path and adding this activity
                    path[t][b] = path[t - t_cost][b - b_cost] + [[name, t_cost, b_cost, enjoyment]]

    # where the maximum enjoyment is located 
    best_t, best_b = np.unravel_index(np.argmax(dp), dp.shape)
    return path[best_t][best_b],dp[best_t][best_b],best_t,best_b
