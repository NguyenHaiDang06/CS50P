import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    students=[]
    try:
        with open(sys.argv[1], "r") as file:

            reader = csv.DictReader(file)
            for row in reader:
                last,first=row["name"].split(", ")
                students.append({"first":first,"last":last,"house":row["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    with open(sys.argv[2], "w") as file:
        header=["first", "last", "house"]
        writer=csv.DictWriter(file, fieldnames=header)

        writer.writeheader()
        for student in students:
            writer.writerow(student)      

if __name__=="__main__":
    main()
