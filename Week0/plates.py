def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (2<=len(s)<=6 and s[0].isalpha() and s[1].isalpha()):
        return False
    if not s.isalnum():
        return False
    found_number=False    
    
    for i in s:
        if i.isdigit():
           if not found_number and i=="0":
               return False
           found_number=True
        elif found_number and i.isalpha():
            return False
            
    return True    
    
main()
