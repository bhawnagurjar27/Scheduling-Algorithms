
#include<stdio.h>                                                        // Function to find the waiting time for all processes
void WaitingTime(int processes[], int n, int burst_time1[], int waiting_time[])  
{                                                                    
    waiting_time[0] = 0;                                            // waiting time for first process is 0  
    
   
    for (int  i = 1; i < n ; i++ )  {                       // calculating waiting time  
        waiting_time[i] =  burst_time1[i-1] + waiting_time[i-1] ;  
}  
}
    

void TurnAroundTime( int processes[], int n, int burst_time1[], int waiting_time[], int turn_around_time[])         // Function to calculate turn around time   
{  
    for (int  i = 0; i < n; i++) {
        turn_around_time[i] = burst_time1[i] + waiting_time[i];  
    }
}  
    
//Function to calculate average time  
void averagetime( int processes[], int n, int burst_time1[])  
{  
    int waiting_time[n], turn_around_time[n], total_waiting_time = 0, total_turn_around_time = 0;  
    
    
    WaitingTime(processes, n, burst_time1, waiting_time);  
    TurnAroundTime(processes, n, burst_time1, waiting_time, turn_around_time);  
    
    printf("Processes Burst time  Waiting time Turn around time\n");  
    
    for (int  i=0; i<n; i++)  
    {  
        total_waiting_time = total_waiting_time + waiting_time[i];  
        total_turn_around_time = total_turn_around_time + turn_around_time[i];  
        printf("   %d ",(i+1)); 
        printf("       %d ", burst_time1[i] ); 
        printf("       %d",waiting_time[i] ); 
        printf("       %d\n",turn_around_time[i] );  
    }  
    float average_waiting_time = (float)total_waiting_time / (float)n; 
    float average_turn_around_time=(float)total_turn_around_time / (float)n; 
    printf("Average waiting time = %.1f",average_waiting_time); 
    printf("\n"); 
    printf("Average turn around time = %.1f",average_turn_around_time);  
}  
    

int main()  
{  
    int number_of_processes;
    scanf("%d",&number_of_processes);
    int processes[number_of_processes];  
    int n = sizeof processes / sizeof processes[0];  
    
    for(int i = 0; i < n; i++){
        scanf("%d",&processes[i]);
        //scanf("%d",&burst_time1[i]);
            
        }
      int burst_time1[n]; 
      for(int i = 0; i<n; i++){
          scanf("%d", &burst_time1[i]);
      }
    
    
    averagetime(processes, n,  burst_time1);  
    return 0;  
}  
