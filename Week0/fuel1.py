import sys

def main():
    fraction = input("Fraction: ")
    try:
        percentage = convert(fraction)
        print(gauge(percentage))
    except (ValueError, ZeroDivisionError):

        sys.exit()

def convert(fraction):

    x_str, y_str = fraction.split("/")
    

    x = int(x_str)
    y = int(y_str)

    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError
        

    return round((x * 100) / y)

def gauge(percentage):

    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
