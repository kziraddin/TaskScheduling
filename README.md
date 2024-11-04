## Task Scheduling Problem
This project contains a solution to the "Task Scheduling" problem, where we have a list of tasks with different deadlines and durations. The goal is to schedule the tasks in a way that minimizes the maximum delay of any task relative to its deadline.

### Problem Description
You have T tasks to complete today. For each task i:

M represents the time required to complete it.
D represents the deadline by which it should ideally be completed.

### Constraints
1 ≤ 𝑇 ≤ 10^5
1 ≤ 𝐷𝑖 ≤ 10^5
1 ≤ 𝑀𝑖 ≤ 10^3

Tasks do not have to be completed consecutively; you can pause a task, work on another, and return to it later. Given that it may not be possible to finish all tasks within their respective deadlines, the objective is to minimize the maximum amount by which any task's completion time exceeds its deadline.

### Input Format
The first line contains an integer T, the number of tasks.
Each of the next T lines contains two integers, D and M, for each task's deadline and time required.

### Output Format
For each task, output the maximum delay at that step if the tasks are scheduled optimally.

### Example Input
5
2 2
1 1
4 3
10 1
2 1

### Example Output
0
1
2
2
3

### Solution Explanation
The solution involves:

1. Sorting Tasks by Deadline: To minimize delays, tasks with earlier deadlines are processed first.
2. Scheduling Logic:
 As each task is added, current_time is updated by adding the task's duration.
 The delay for each task is calculated by checking if current_time overshoots the task's deadline.
 max_delay is updated to store the maximum delay encountered across all tasks scheduled up to that point.

### Code
import os

def taskScheduling(tasks):
    # Sort tasks by their deadlines
    tasks.sort()
    
    current_time = 0
    max_delay = 0
    
    for d, m in tasks:
        current_time += m  # Add task's duration to current time
        delay = max(0, current_time - d)  # Calculate delay if any
        max_delay = max(delay, max_delay)  # Update max delay if needed
        
    return max_delay

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read input
    t = int(input().strip())
    tasks = []
    
    for _ in range(t):
        d, m = map(int, input().rstrip().split())
        tasks.append((d, m))
        
        result = taskScheduling(tasks)
        fptr.write(str(result) + '\n')

    fptr.close()

Running the Program
Input: Prepare a list of tasks with deadlines and required times.
Execution: Run the script. It reads input in the format described above and outputs the maximum delay after each task is scheduled.
Output: For each task, you receive the maximum delay observed so far.
Example Run
If you run the script with the example input provided, it should produce:

0
1
2
2
3


### Complexity Analysis
Time Complexity: O(TlogT) due to sorting the tasks by deadline.
Space Complexity: O(T) for storing task details.
