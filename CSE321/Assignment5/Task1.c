#include<stdio.h>
static int mark[30];
int i,j,np,nr;
int main()
{
int r[20],w[20];
int n, m;
n = 5;
m = 4;
int alloc[5][4] = { { 0, 1, 0, 3 },
{ 2, 0, 0, 0 },
{ 3, 0, 2, 0 },
{ 2, 1, 1, 5 },
{ 0, 0, 2, 2 } };
int max[5][4] = { { 6, 4, 3, 4 },
{ 3, 2, 2, 1 },
{ 9, 1, 2, 6 },
{ 2, 2, 2, 8 },
{ 4, 3, 3, 7 } };
int avail[4] = { 3, 3, 2, 1 };
for(j=0;j<nr;j++)
{
avail[j]=r[j];
for(i=0;i<np;i++)
{
avail[j]-=alloc[i][j];
}
}

for(i=0;i<np;i++)
{
int count=0;
for(j=0;j<nr;j++)
{
if(alloc[i][j]==0)
count++;
else
break;

}
if(count==nr)
mark[i]=1;
}
for(j=0;j<nr;j++)
w[j]=avail[j];

for(i=0;i<np;i++)
{
int canbeprocessed=0;
if(mark[i]!=1)
{
for(j=0;j<nr;j++)
{
if(max[i][j]<=w[j])
{
canbeprocessed=1;
}
else
{
canbeprocessed=0;
break;
}
}
if(canbeprocessed)
{
mark[i]=1;
for(j=0;j<nr;j++)
w[j]+=alloc[i][j];
}
}
}

int deadlock=0;
for(i=0;i<np;i++)
if(mark[i]!=1)
deadlock=1;

if(deadlock)
printf("\n Deadlock detected");

else
printf("\n Safe here");
}