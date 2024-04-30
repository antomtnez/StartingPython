number = int(input("Introduce un edad: "))
overTwenty = number > 19
underThirty = number <= 30
if overTwenty and underThirty:
    print("Estas entre los 20's y los 30's")
else:
    print("No estas entre los 20's y los 30's")