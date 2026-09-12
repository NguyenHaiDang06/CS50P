import random
def main():
   level=get_level()
   score=0
   for _ in range(10):
      x=generate_integer(level)
      y=generate_integer(level)
      errors = 0
      while True:
         try:
            guess=int(input(f"{x} + {y} = "))
            if guess == x + y:
               score += 1
               break
            else:
               print("EEE")
               errors += 1
         except ValueError:
            print("EEE")
            errors += 1
         if errors == 3:
            print(f"{x} + {y} = {x + y}")    
            break

   print(f"Score: {score}")              
def get_level():
    while True:
        try:
          a=int(input("Level: "))
          if a in [1, 2, 3]:
             return a
        except ValueError:
           pass  
def generate_integer(level):
   if level == 1:
      return random.randint(0, 9)
   elif level == 2:
      return random.randint(10, 99)
   elif level == 3:
      return random.randint(100, 999)
   else:
      raise ValueError       

if __name__ == "__main__":
    main()   
