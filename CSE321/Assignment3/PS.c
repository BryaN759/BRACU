#include <stdio.h>
int main(){
    int arrivalTime[12];
    int burstTime[12];
    int remainingTime[12];
    int priority[12];
    int shortest, done, num, wait, turnaround;
    int remain=0;

    printf("Enter number of processes: ");
    scanf("%d",&num);
    for (int i=0;i<num;i++){
        printf("Enter arrival, burst and priority time of process %d: ",i+1);
        scanf("%d %d %d",&arrivalTime[i],&burstTime[i],&priority[i]);
        remainingTime[i]=burstTime[i];

    }
    priority[10]=100;
    shortest=10;

    for (int time=0;remain!=num;time++){

        for (int j=0;j<num;j++){
            if (arrivalTime[j]<=time && remainingTime[j]>0 && priority[j]<priority[shortest]){
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

