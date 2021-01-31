def waitingTime(processes, length_of_processes, waiting_time):  
    remaining_time = [0] * length_of_processes 
  
    # Copy the burst time into remaining_time[]  
    for i in range(length_of_processes):  
        remaining_time[i] = processes[i][1] 
    
    complete = 0
    time = 0
    minm = 999999999
    short = 0
    check = False
  
    while (complete != length_of_processes):                                   # Process until all processes gets completed  
          
        for j in range(length_of_processes): 
            if ((processes[j][2] <= time) and 
                (remaining_time[j] < minm) and remaining_time[j] > 0): 
                minm = remaining_time[j] 
                short = j 
                check = True
        if (check == False): 
            time += 1
            continue
              
        remaining_time[short] -= 1
  
        minm = remaining_time[short]                                             # Update minimum  
        if (minm == 0):  
            minm = 999999999
  
        if (remaining_time[short] == 0):                                         # If a process gets completely executed  
            complete += 1
            check = False
  
            finish_time_current_process = time + 1                                                         # Find finish time of current process  
  
            # Calculate waiting time  
            waiting_time[short] = (finish_time_current_process - processes[short][1] - processes[short][2]) 
  
            if (waiting_time[short] < 0): 
                waiting_time[short] = 0
          
        # Increment time  
        time += 1
  
# Function to calculate turn around time  
def turnAroundTime(processes, length_of_processes, waiting_time, turn_around_time):  
      
    for i in range(length_of_processes): 
        turn_around_time[i] = processes[i][1] + waiting_time[i]  
  
# Function to calculate average waiting and turn-around times.  
def averageTime(processes, length_of_processes):  
    waiting_time = [0] * length_of_processes
    turn_around_time = [0] * length_of_processes  
  
    # Function to find waiting time of all processes  
    waitingTime(processes, length_of_processes, waiting_time)  
  
    # Function to find turn around time for all processes  
    turnAroundTime(processes, length_of_processes, waiting_time, turn_around_time)  
 
    print("Processes    Burst Time     Waiting Time     Turn-Around Time") 
    total_waiting_time = 0
    total_turn_around_time = 0
    
    for i in range(length_of_processes): 
  
        total_waiting_time = total_waiting_time + waiting_time[i]  
        total_turn_around_time = total_turn_around_time + turn_around_time[i]  
        print(" ", processes[i][0], "\t\t", processes[i][1], "\t\t", waiting_time[i], "\t\t", turn_around_time[i]) 
  
    print("\nAverage waiting time = %.5f "%(total_waiting_time /length_of_processes) ) 
    print("Average turn around time = ", total_turn_around_time / length_of_processes)  
      
      
number_of_testcases = int(input())

for _ in range(number_of_testcases):
    number_of_processes = int(input())
    processes = [[1, 6, 1], [2, 8, 1], [3, 7, 2], [4, 3, 3]] 
    burst_time = list(map(int, input().split()))
    # considering that arrival time for all processes is 0
    
    length_of_processes = len(processes)
    averageTime(processes, length_of_processes) 
      