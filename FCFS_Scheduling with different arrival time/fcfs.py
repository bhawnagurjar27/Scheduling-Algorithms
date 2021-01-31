def waitingtime(processes, burst_time, waiting_time, length_of_processes, arrival_time):
    total_time = [0] * length_of_processes                               # Function to find the waiting time for all processes 
    total_time[0] = 0                                                     # burst time of previous processes 
    waiting_time[0] = 0
    for i in range(1, length_of_processes):
        total_time[i] = (total_time[i - 1] + burst_time[i - 1])                           # calculating waiting time 
        waiting_time[i] = total_time[i] - arrival_time[i]                                 

        if (waiting_time[i] < 0):
            waiting_time[i] = 0                                     
        

def turnaroundtime(turn_around_time, processes, burst_time, waiting_time, length_of_processes):
    
    for i in range(length_of_processes):
        turn_around_time[i] = waiting_time[i] + burst_time[i]                                     #calulating turn_around_time of processes
        

def averagetime(processes, length_of_processes, burst_time, arrival_time):
    
    total_waiting_time = 0
    total_turn_around_time = 0
    
    waiting_time = [0]*length_of_processes
    turn_around_time = [0]*length_of_processes
    
    waitingtime(processes, burst_time, waiting_time, length_of_processes, arrival_time)                         #function to find waiting time for all processes
    turnaroundtime(turn_around_time, processes, burst_time, waiting_time, length_of_processes)                  #function to find turn around time for all processes

    #print( "Processes Burst time " +  " Waiting time " + " Turn around time")
    print("Processes Burst Time Arrival Time   Waiting", "Time Turn-Around Time Completion Time ") 
    
    for i in range(length_of_processes):
        total_waiting_time = total_waiting_time + waiting_time[i]
        total_turn_around_time = total_turn_around_time + turn_around_time[i]
        completion_time = turn_around_time[i] + arrival_time[i] 
        print(" " + str(i + 1) + "\t\t" +  str(burst_time[i]) + "\t " + str(waiting_time[i]) + "\t\t" + str(turn_around_time[i]) + "\t\t" + str(completion_time))  

    average_waiting_time = total_waiting_time / length_of_processes
    average_turn_around_time = total_turn_around_time / length_of_processes
    
    
    print( "Average waiting time = "+str(average_waiting_time)) 
    print("Average turn around time = "+str(average_turn_around_time)) 



number_of_testcases = int(input())

for _ in range(number_of_testcases):
    number_of_processes = int(input())
    processes = list(map(int,input().split()))
    burst_time = list(map(int, input().split()))
    # considering that arrival time for all processes is 0
    arrival_time = list(map(int, input().split()))
    
    length_of_processes = len(processes)
    averagetime(processes, length_of_processes, burst_time, arrival_time)