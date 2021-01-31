
#include <stdio.h>
void WaitingTime(int processes[], int n, int burst_time[], int waiting_time[], int arrival_time[])
{
	int i, service_time[n];
	service_time[0] = 0;
	waiting_time[0] = 0;
	for ( i = 1; i < n ; i++)
	{
		service_time[i] = service_time[i-1] + burst_time[i-1];
		waiting_time[i] = service_time[i] - arrival_time[i];
		if (waiting_time[i] < 0)
		waiting_time[i] = 0;
	}
}

void TurnAroundTime(int processes[], int n, int burst_time[], int waiting_time[], int turn_around_time[])
{
    int i;
	for ( i = 0; i < n ; i++)
	turn_around_time[i] = burst_time[i] + waiting_time[i];
}

void AverageTime(int processes[], int n, int burst_time[], int arrival_time[])
{
	int i, waiting_time[n], turn_around_time[n];

	WaitingTime(processes, n, burst_time, waiting_time, arrival_time);

	TurnAroundTime(processes, n, burst_time, waiting_time, turn_around_time);

	printf("Processes\tBurst Time\tArrival Time\tWaiting Time\tTurn Aounr Time\tCompletion Time\n");
	int total_waiting_time = 0, total_turn_around_time = 0;
	for ( i = 0 ; i < n ; i++)
	{
		total_waiting_time = total_waiting_time + waiting_time[i];
		total_turn_around_time = total_turn_around_time + turn_around_time[i];
		int completion_time = turn_around_time[i] + arrival_time[i];
		printf("\t%d\t%d\t%d\t%d\t%d\t%   d\n", (i+1), burst_time[i], arrival_time[i], waiting_time[i], turn_around_time[i], completion_time);
	}

	printf("Average waiting time = %f\n", (float)total_waiting_time / (float)n);
	printf("Average turn around time = %f\n", (float)total_turn_around_time / (float)n);
}


int main()  
{  
    int number_of_processes, i;
    scanf("%d\n",&number_of_processes);
    int processes[number_of_processes];  
    int n = sizeof processes / sizeof processes[0];  
    for( i = 0; i < n; i++){
        scanf("%d",&processes[i]);
     }
      int burst_time[n];
      int arrival_time[n]; 
      for( i = 0; i<n; i++){
          scanf("%d", &burst_time[i]);
          //scanf("%d", &arrival_time[i]);
      }
      for( i = 0; i<n; i++){
          scanf("%d\n",&arrival_time[i]);
          //scanf("%d", &arrival_time[i]);
      }
    
    
    AverageTime(processes, n,  burst_time, arrival_time);  
    return 0;  
}  
