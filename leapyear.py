year = int(input("Enter year: "))

if year % 4 and year % 100 != 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


