for number in range(6):
    if number%2 == 0:
        print(f"Value: {number}")

for number in range(6):
    if number%2 != 0:
        continue    
    print(f"Value: {number}")