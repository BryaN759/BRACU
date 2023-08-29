import random

n=input("Enter Student ID of 8 digits: ")
ID=[]
for i in n:
    if i=='0':
        ID.append(8)
    else:
        ID.append(int(i))

min_point=ID[4]
max_point=int((ID[-1]*10+ID[-2])*1.5)
win_point=(ID[-1]*10+ID[-2])
shuffle_num=int(ID[3])


def AlphaBeta(level, index, isMaximizingPlayer, value, alpha, beta):
    if level == 3:
        return value[index]
    if (isMaximizingPlayer==True):
        largest_node = -1000
        for i in range(2):
            val   = AlphaBeta(level + 1, index * 2 + i,False, value, alpha, beta)
            largest_node  = max(largest_node, val)
            alpha = max(alpha, largest_node)
            if beta <= alpha:
                break;
        return largest_node
    if (isMaximizingPlayer == False):
        largest_node = 1000
        for i in range(2):
            val  = AlphaBeta(level + 1, index * 2 + i,True, value, alpha, beta)
            largest_node = min(largest_node, val)
            beta = min(beta, largest_node)
            if beta <= alpha:
                break;
        return largest_node

def points_generator(max_point,min_point):
    random_points=[]
    for i in range(8):
        random_points.append(random.randint(min_point,max_point))
    return random_points

l=points_generator(max_point,min_point)
print("Generated 8 random points between the minimum and maximum point limits:",l)
print("Total points to win:",win_point)

def task1(win_point):
    global l
    x=AlphaBeta(0,0,True,l,-1000,1000)
    print("Achieved point by applying alpha-beta pruning",x)
    if x>=win_point:
        print("Optimus Prime Wins")
    else:
        print("Megatron Wins")

def task2(shuffle_num,win_point):
    points=[]
    win_rate=0

    global l
    for i in range(shuffle_num):
        random.shuffle(l)
        x = AlphaBeta(0, 0, True, l, -1000, 1000)
        points.append(x)
    for i in points:
        if i>=win_point:
            win_rate+=1

    print("List of all points values from each shuffle:",points)
    print("The maximum value of all shuffles",max(points))
    print("Won {} times out of {} times".format(win_rate,len(points)))

task1(win_point)
task2(shuffle_num,win_point)

















