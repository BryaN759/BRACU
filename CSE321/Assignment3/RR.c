#include <stdio.h>
int main(){

    int burstTime[10];
    int remainingTime[10];
    int shortest=100;
    int num, count, wait, turnaround;
    int remain=0;
    printf("Enter number of processes: ");
    scanf("%d",&num);
    for (int i=0;i<num;i++){
        printf("Enter burst time of process %d: ",i+1);
        scanf("%d",&burstTime[i]);
        remainingTime[i]=burstTime[i];

    }
    while(1){
        for (int j=0,count=0;j<num;j++){
            int x=shortest;
            if (remainingTime[j]==0){
                count++;
                continue;


            }
            if (remainingTime[j]>=shortest){
                remainingTime[j]=remainingTime[j]-shortest;
            }
            else
                if(remainingTime[j]>=0){

                    x=remainingTime[j];
                    remainingTime[j]=0;
                }
                remain=remain+x;
                turnaround=remain;
                if (remainingTime[j]==0){
                    wait=turnaround-burstTime[j];
                    printf("process%d: Completion time:%d Turnaround time: %d Waiting time: %d\n",j+1,turnaround,turnaround,wait);
                    wait=0;


                }

            }

        if(num==count){
            break;
        }


        }
    }












