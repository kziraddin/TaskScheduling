'''You have a long list of tasks that you need to do today. To accomplish task i you need M; minutes, 
and the deadline for this task is Di. You need not complete a task at a stretch. 
You can complete a part of it, switch to another task, and then switch back.
You've realized that it might not be possible to complete all the tasks by their deadline. 
So you decide to do them in such a manner that the maximum amount by which a task's completion time overshoots 
its deadline is minimized.

Input Format

The first line contains the number of tasks, T. Each of the next T lines contains two integers, D; and Mi.

Constraints
1ST ≤ 105
1≤ Di ≤ 105
1 ≤ Mi ≤ 103

Output Format
Output T lines. The ith line contains the value of the maximum amount by which a task's completion time overshoots its deadline, 
when the first i tasks on your list are scheduled optimally. See the sample input for clarification.

Sample Input
5
22
11
4 3
10 1
21

Sample Output
1
2
2
3

Explanation

The first task alone can be completed in 2 minutes, and so you won't overshoot the deadline.
With the first two tasks, the optimal schedule can be:
time 1: task 2
time 2: task 1
time 3: task 1

We've overshot task 1 by 1 minute, hence returning 1.
With the first three tasks, the optimal schedule can be:

time 1: task 2
time 2 : task 1
time 3: task 3
time 4: task 1
time 5: task 3
time 6: task 3

Task 1 has a deadline 2, and it finishes at time 4. So it exceeds its deadline by 2.
0.
2.

Task 2 has a deadline 1, and it finishes at time 1. So it exceeds its deadline by
Task 3 has a deadline 4, and it finishes at time 6. So it exceeds its deadline by
Thus, the maximum time by which you overshoot a deadline is 2. No schedule can do better than this.
Similar calculation can be done for the case containing 5 tasks.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'taskScheduling' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER m
#

def taskScheduling(tasks):
    # Write your code here
    tasks.sort()
    
    current_time = 0
    max_delay = 0
    
    for d, m in tasks:
        current_time += m #m is required time (duration)
        delay = max(0, current_time - d) #d - deadline
        max_delay = max(delay, max_delay)
        
    return max_delay
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())
    tasks = []
    
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        d = int(first_multiple_input[0])

        m = int(first_multiple_input[1])
        
        tasks.append((d,m))
        
        result = taskScheduling(tasks)

        fptr.write(str(result) + '\n')

    fptr.close()
