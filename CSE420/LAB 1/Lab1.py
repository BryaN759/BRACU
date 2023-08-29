o=open(r"lab1.txt",'r')
r=o.read()
r=r.split()


keywords=("")    
keys=["and", "as", "assert", "break", "class", "continue", "def", "del", "elif", "else", "except", "False",  "finally", "not", "for", "from", "global", "if", "import", "in", "is", "lambda", "None", "nonlocal", "not", "or", "pass", "raise", "return", "True", "try", "while", "with", "yield", "int", "float"]
maths=("")
mathop=["+", "-", "/", "//", "*", "**" , "="]
numbers=("")
logical=("")
operators=[">", "<", ">=", "<=", "==", "!="]
other=("")
others=[",", ";", "(", ")", "{", "}"]
identifier=("")
#=======

#For Numerical Values
for i in r:
    try:
        float(i)
        for k in r:
            if i not in numbers:
                numbers+= (i) + (",")
    except:
        None


for i in r:
#For Keywords
    if i in keys:
        if i not in keywords:
            keywords+= (i) + (",")
#For Math Operators    
    elif i in mathop:
        if i not in maths:
            maths+= (i) + (",")
#For Logical Operators
    elif i in operators:
        if i not in logical:
            logical+= (i) + (",")
#For Others
    elif i in others:
        if i not in other:
            other+= (i) + (" ")
#For Identifiers
    elif (ord(i[0])>=65 and ord(i[0])<=90) or (ord(i[0])>=97 and ord(i[0])<=122) or ord(i[0])==95:
            lenth=len(i)
            if len(i)==1:
                if i not in identifier:
                    identifier+= (i) + (",")
            else:
                for k in range (1,lenth):
                    if (ord(i[k])>=65 and ord(i[k])<=90) or (ord(i[k])>=97 and ord(i[k])<=122) or (ord(i[k])==95) or (ord(i[k])>=0 and ord(i[k])<=9):
                        if i not in identifier:
                            identifier+= (i) + (",")
                            


f=open("lab1_out.txt",'w')                            
f.write("Keywords: " + (keywords.rstrip(","))+"\n")
f.write("Identifiers: " + (identifier.rstrip(","))+"\n")
f.write("Math Operator: " + (maths.rstrip(","))+"\n")
f.write("Logical Opertators: " + (logical.rstrip(","))+"\n")
f.write("Numerical Values: " + ((numbers.rstrip(",")))+"\n")
f.write("Others: " + (other) + "\n")