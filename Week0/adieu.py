import inflect

name=[]
p=inflect.engine()
while true:
     try:
       name=input("Name: ")
       names.append(name)
     except EOFError:
       print()
       break;

print("Adieu, adieu, to "+ p.join(names))
  
