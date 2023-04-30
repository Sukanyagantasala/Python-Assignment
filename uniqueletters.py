string=input("Enter a string : ")
l=[]
for i in string:
    if i not in l:
        l.append(i)
    output=','.join(l)
print(output)