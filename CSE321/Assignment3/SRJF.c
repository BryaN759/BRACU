// Online C compiler to run C program online
#include <stdio.h>
int main(){
    int arrivalTime[10];
    int burstTime[10];
    int remainingTime[10];
    int shortest, done, num, wait, turnaround;
    int remain=0;
    
    printf("Enter number of processes: ");
    scanf("%d",&num);
    for (int i=0;i<num;i++){
        printf("Enter arrival and burst time of process %d: ",i+1);
        scanf("%d %d",&arrivalTime[i], &burstTime[i]);
        //printf("Enter burst time of process %d: ",i+1);
        //scanf("%d",&burstTime[i]);
        remainingTime[i]=burstTime[i];

    }
    remainingTime[10]=100;
    shortest=10;

    for (int time=0;remain!=num;time++){

        for (int j=0;j<num;j++){
            if (arrivalTime[j]<=time && remainingTime[j]>0 && remainingTime[j]<remainingTime[shortest]){
                shortest=j;
            }
        }
        remainingTime[shortest]--;
        if (remainingTime[shortest]==0){
            remain=remain+1;
            done=time+1;
            turnaround=done-arrivalTime[shortest];
            wait=turnaround-burstTime[shortest];

            printf("process%d: Completion time:%d Turnaround time: %d Waiting time: %d\n",shortest+1,done,turnaround,wait);
            done=0;
            turnaround=0;
            wait=0;
            shortest=10;




        }

    }
}
