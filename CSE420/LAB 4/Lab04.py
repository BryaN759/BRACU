

import re

f = open("input.txt", "r")
code = f.readlines()
method = []
mainMethod = r"public static void main(.*)"
regex = r"(public|private|default)( static)? (Boolean|char|byte|short|int|long|float|double|String|void) \w+\((.*)?\)"
for i in code:
    if re.match(regex, i) and not re.match(mainMethod, i):
        method.append(re.findall("(Boolean|char|byte|short|int|long|float|double|String|void) (\w+)\((.+)?\)", i)[0])

print("Methods:")
for i in method:
    print("{} ({}), return type: {}".format(i[1], i[2], i[0]))


