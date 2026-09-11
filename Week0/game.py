import random

while True:
    try:
        p=int(input("Level: "))
        if p>0:
          break
    except ValueError:
        pass

a=random.randint(1, p)

while True:
    try:
        guess = int(input("Guess: "))


        if guess > 0:


            if guess < a:
                print("Too small!")
            elif guess > a:
                print("Too large!")
            else:
                print("Just right!")
                break

    except ValueError:
        pass      
