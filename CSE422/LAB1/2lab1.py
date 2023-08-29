with open('2input2.txt', 'r') as file:
   lines = file.readlines()
mtx=[]
row = int(lines[0])
column = int(lines[1])
lines=lines[2:]
for line in lines:
    for word in line:
        x = line.split()
    mtx.append(x)


def attacks(matrix,vis,stack):
    count=-1
    global row
    global column
    while len(stack)!=0:
        t=len(stack)
        for k in range(t):
            r,c=stack.pop(0)
            for i in range(-1, 2):
                for j in range(-1,2):
                    if i!=j and i + j!=0:
                        if r + i  < 0 or c + j < 0 or r + i >=row or c + j >=column or matrix[r + i][c + j]!='H':  # check if out of bound
                            False
                        else:
                            if [r + i,c + j] not in vis:
                                vis.append([r + i,c + j])
                                stack.append([r + i,c + j])
                                matrix[r + i][c + j] = 'A'
        count+=1
    return count



def numofhumans_survived(matrix,r,c):
    vis=[]
    stack=[]


    for row in range(r):
            for col in range(c):
                if matrix[row][col] == 'A':
                    stack.append([row,col])

    ans=attacks(matrix,vis,stack)
    print('Time- '+ str(ans)+' minuties')
    h=0
    for pairs in matrix:
        for i in pairs:
            if i=='H':
                h+=1
    if h==0:
        print('No one survived')
    else:
        print(h,'survived')
numofhumans_survived(mtx,row,column)