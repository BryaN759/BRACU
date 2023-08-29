numbers = '0123456789'
alpha = 'abcdefghijklmnopqrstuvwxyz'

def email_check(string):
    global numbers, alpha
    state = 0
    for i in string:
        if state == 0:
            if i in alpha:
                state = 1
                continue
            else:
                print("Invalid input")
                break
        if state == 1:
            if i in alpha or numbers:
                state = 1
            if i == '@':
                state = 2
                continue
        if state == 2:
            if i in alpha:
                state = 3
                continue
            else:
                print("Invalid input")
                break
        if state == 3:
            if i in alpha:
                state = 3
            if i == '.':
                state = 4
                continue
        if state == 4:
            if i in alpha:
                state = 5
                continue
            else:
                print("Invalid input")
                break
        if state == 5:
            if i in alpha:
                state = 5
            if i == '.':
                state = 4

    if state == 5:
        return 1
    else:
        return 0


def web_check(string):
    global numbers, alpha
    state = 0
    for i in string:
        if state == 0:
            if i == 'w':
                state = 1
                continue
            else:
                break
        if state == 1:
            if i == 'w':
                state = 2
                continue
            else:
                break
        if state == 2:
            if i == 'w':
                state = 3
                continue
            else:
                break
        if state == 3:
            if i == '.':
                state = 4
                continue
            else:
                break
        if state == 4:
            if i in alpha:
                state = 5
                continue
            else:
                break
        if state == 5:
            if i in alpha or numbers:
                state = 5
            if i == '.':
                state = 6
                continue
        if state == 6:
            if i in alpha:
                state = 7
                continue
            else:
                break
        if state == 7:
            if i in alpha:
                state = 7
            if i == '.':
                state = 6

    if state == 7:
        return 1
    else:
        return 0


inputs = [4, 'moon@gmail.com', 'www.naziaislam.com', 'www.naziaislam.co.us', 'nazia.islam@g.bracu.ac.bd']

for i in range(1, inputs[0] + 1):
    string = inputs[i]
    email = email_check(string)
    web = web_check(string)
    if email == 0 and web == 0:
        print("Invalid input,", i)
    elif email == 1:
        print("Email,", i)
    elif web == 1:
        print("Web,", i)