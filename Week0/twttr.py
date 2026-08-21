a=input("Input:")
x="aeiouAEIOU"
print("Output:",end="")
for b in a:
    if b in x:
        continue
    print(b,end="")
print() 
