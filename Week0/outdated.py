months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
      date = input("Date: ")
 
      if "/" in date:
         month, day, year = date.split("/")
   
         month = int(month)
         day = int(day)
         year = int(year)
      else:
         month, day, year = date.split(" ")

         if not day.endswith(","):
            continue

         day = day.strip(",")
         month = months.index(month) + 1
         day = int(day)
         year = int(year)
      if 1<=month<=12 and 1<=day<=31:
         print(f"{year}-{month:02}-{day:02}") 
         break
    except (ValueError,IndexError):
        pass
    
        
