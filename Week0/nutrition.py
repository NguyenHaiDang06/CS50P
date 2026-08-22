fruits={
    "apple":130,
    "avocado":50,
    "banana":110,
    "kiwifruit": 90,
    "pear": 100,
    "sweet cherries": 100
}
a=input("Item: ").lower()
if a in fruits:
    print("Calories: ",fruits[a])
