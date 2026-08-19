a=input("camelCase: ")
print("snake_case: ",end="")
for i in a:
    if i.isupper():
        print("_"+i.lower(),end="")
    else:
        print(i,end="")
print()
