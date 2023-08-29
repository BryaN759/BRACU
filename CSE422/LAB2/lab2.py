import random

p=[]
r=[]
x=input().split()
players_n=int(x[0])
target=int(x[1])
for i in range(players_n):
    y=input().split()
    p.append(y[0])
    r.append(int(y[1]))
#print(p,r)

def GA():
    population=populate()
    population=crossover(population)
    population=mutation(population)
    print(population)
    selection(population)

def populate():
    global players_n
    pp=[]
    x=""
    for i in range(100):                 #to have atleast 50 data sets
        for j in range(players_n):
            x+=str(random.randrange(0,2))
        f=fitness(x)
        if f>0:
            pp.append(x)
            x = ""
        else:
            x = ""
    return pp


def crossover(pp):
    global players_n
    for i in range(0, len(pp) - 1, 2):
        m1 = pp[i][:players_n//2] + pp[i + 1][players_n//2:len(pp[i])]
        m2 = pp[i + 1][:players_n//2] + pp[i][players_n//2:len(pp[i])]
        #print(m1,m2)
        f=fitness(m1)
        if f>0:
            pp[i] = m1
        f=fitness(m2)
        if f>0:
            pp[i + 1] = m2
    return pp

def mutation(pp):
    global players_n
    l = []
    for i in pp:
        x = random.randrange(players_n)         # getting a random index where mutation is to be performed
        if i[x]=='1':
            i=i[:x]+'0'+i[x+1:]
        elif i[x]=='0':
            i=i[:x]+'1'+i[x+1:]
        f = fitness(i)                          # checking fitness again then sending to population
        if f > 0:
            l.append(i)
    return l


def fitness(bin):
    global p,r,target,players_n
    runs=0
    for i in range(players_n):
        if bin[i]=='1':
            runs+=r[i]
    if runs>=target:
        return 1
    else:
        return -1


def selection(pp):
    global p,r,target
    players=[]
    runs=0
    for i in pp:
        for j in range(len(i)):
            if i[j]=='1':
                runs+=r[j]
                players.append(p[j])
        if runs==target:
            print(players)
            print(i)
            break
        else:
            runs=0
            players.clear()


GA()

