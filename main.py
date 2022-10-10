year = int(input("Enter Year / Adj meg egy évszámot: "))

# Leap Year Check/ Szökőév meghatározása
if year % 4 == 0 and year % 100 != 0:
    print(year, " is a Leap Year / Szökőév !")
elif year % 400 == 0:
    print(year, "is  a Leap Year / Szökőév !")
elif year % 100 ==0:
    print(year, "is not a Leap Year / Nem Szökőév")
else:
    print(year, "is not a Leap Year / Nem szökőév!")