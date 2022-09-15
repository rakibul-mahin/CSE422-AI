'''
CONSTRAINTS

1. There is going to be 4 levels
2. Level 0 -> Max -> Optimus Prime
3. Level 1 -> Min -> Megatron
4. Level 2 -> Max -> Optimus Prime
5. Level 3 -> Min -> Megatron

*Any digit with 0 will get converted to 8

Minimum Point = 4th index of the ID
Maximum Point = Reverse last 2 digit and multiply with 1.5
Target = Reverse last 2 digit
Number of Shuffle = 3rd index of the ID

My ID: 20201220

28281228
Minimum Point = 1
Maximum Point = 82 * 1.5 = 123
Target = 82
Shuffle = 8
'''

import random
import math

my_id = input("Please Enter Your ID: ").replace('0','8')
# In this part we will extract all the information from the user input
min_point = int(my_id[4])
target_point = my_id[-2:]
target_point = int(target_point[::-1])
max_point = math.ceil(target_point * 1.5)
shuffle_number = int(my_id[3])

# print(f"ID: {my_id}\nMin Point: {min_point}\nMax Point: {max_point}\nTarget Point: {target_point}\nShuffle Number: {shuffle_number}")

# Initializing alpha as -ve infinity and beta as positive infinity
alpha, beta = float('-inf'), float('+inf')

# This function will calculate the total number of wins by Optimus Prime
def calculate_number_of_wins_for_optumus_prime(score_list: int, target: int) -> int:
    win_count = 0
    for i in score_list:
        if i >= target:
            win_count += 1

    return win_count

# This function compares two values and return the max
def max_compare(val1: int, val2: int) -> int:
    if val1 > val2:
        return val1
    else:
        return val2

# This fucntion compares two values and return the min
def min_compare(val1: int, val2: int) -> int:
    if val1 < val2:
        return val1
    else:
        return val2

# This is the main function that does alpha beta prunning on min-max algorithm
def alpha_beta_pruning(level: int, node: int, isMax: bool, point_list: list, alpha: float, beta: float) -> int:

    #As we are taking 8 leaf nodes, 
    #there won't be more than 4 level 
    #starting from 0 to 3
    if level == 3:
        return point_list[node]

    # This condition checks whether the turn is for max
    if isMax:
        best =  alpha
        # Here children are compared and values are updated
        # Here we use max_compare as it is the turn for max
        # Only value of alpha is updated
        for i in range(0,2):
            curr_score = alpha_beta_pruning(level+1, node*2+i, False, point_list, alpha, beta)
            best = max_compare(best, curr_score)
            alpha = max_compare(best, alpha)

            # This is the point where the prunning is done
            if beta <= alpha:
                break

        return best
    # This is when it is the turn for min
    else:
        best = beta
        # Here children are compared and values are updated
        # Here we use min_compare as it is the turn for min
        # Only value of beta is updated
        for i in range(0,2):
            curr_score = alpha_beta_pruning(level+1, node*2+i, True, point_list, alpha, beta)
            best = min_compare(best, curr_score)
            beta = min_compare(best, beta)

            # This is the point where the prunning is done
            if beta <= alpha:
                break

        return best
        
#=========================================TASK-1 OUTPUT==============================================#
print("#============================================TASK-1 OUTPUT=================================================#")
# 8 random numbers starting from min_point to max_point will be generated for the leaf nodes
point_list = [random.randint(min_point, max_point) for _ in range(8)]
print(f"Generated 8 random points between the minimum and maximum point limits: {point_list}")
print(f"Total points to win: {target_point}")
# Now we will call our alpha_beta_pruning function to calculate the score
score = alpha_beta_pruning(0,0,True,point_list,alpha,beta)
print(f"Achieved point by applying alpha-beta prunning = {score}")
# Now compare the score and display the message accordingly
print("The winner is Optimus Prime") if score >= target_point else print("The winner is Megatron")

#=========================================TASK-2 OUTPUT==============================================#
print("#============================================TASK-2 OUTPUT=================================================#")
all_scores = []
# Run the loops according to the shuffle_number generated from the ID 
for i in range(shuffle_number):
    # 8 random numbers starting from min_point to max_point will be generated for the leaf nodes
    # This point list will be newly generated after every iteration
    point_list = [random.randint(min_point, max_point) for _ in range(8)]
    # Now we will call our alpha_beta_pruning function to calculate the score
    # And then add it to our all_score list
    score = alpha_beta_pruning(0,0,True,point_list,alpha,beta)
    all_scores.append(score)

print(f"After the shuffle:\nList of all points values from each shuffles:{all_scores}")
# We are sorting the list to find the highest score at the end of the list
all_scores.sort()
highest_score = all_scores[-1]
print(f"The maximum value of all shuffles: {highest_score}")
# Finally we will call calculate_number_of_wins_for_optumus_prime function
# and calculate number of times Optimus Prime won
win_count = calculate_number_of_wins_for_optumus_prime(all_scores, target_point)
print(f"Won {win_count} times out of {shuffle_number} number of shuffles")