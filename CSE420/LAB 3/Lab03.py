import re

file = [2,'ab*c*d', 'a*b(cd)+e?f', 3, 'acccd', 'abbbbbcccc', 'bcdcdef']
#file = [3, '[a-c]{3}cab+(da)*f', 'db*a[^def]{2}gh', 'def[k-p]*p+', 5, 'defkmnpmpp', 'acbcabbf', 'pqrstdd', 'dbaabggh', 'dbbbbamkgh']

ex_number = file[0]
input_number = file[ex_number+1]

regexs = []

for i in range(1,input_number):
    regexs.append(file[i])

inputs = []

for i in range(input_number+1,len(file)):
    inputs.append(file[i])
print(regexs, inputs)


for input in inputs:
    valid = 0
    re_number = 0
    for regex in range(len(regexs)):
        if re.search(regexs[regex], input):
            valid = 1
            re_number = regex
            break
        else:
            continue
    if valid == 1:
        print("YES", re_number+1)
    else:
        print("NO", 0)