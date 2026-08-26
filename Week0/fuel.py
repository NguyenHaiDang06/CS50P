while True:
    try:
        fraction=input("Fraction: ")
        x,y=fraction.split("/")
        x=int(x)
        y=int(y)
        if x>y or x<0 or y<0:
           continue
        percent=round((x*100)/y)
    except (ValueError,ZeroDivisionError):
           continue
    if percent <= 1:
        print("E")
    elif percent >= 99:
        print("F")
    else:
        print(f"{percent}%")

    break
