number = int(input("Write a month in number (1 - 12):"))

if 1 <= number < 4:
    seasonText = "Winter"
elif 4 <= number < 7:
    seasonText = "Spring"
elif 7 <= number < 10:
    seasonText = "Summer"
elif 10 <= number < 12:
    seasonText = "Autumn"
else:
    seasonText = "Out of range"
print(f"Month {number} is on {seasonText} season")