print("Welcome, I'm a unit converter, km to miles.")

while True:
    print("Enter the number of kilometers.")
    km = input("Kilometers: ")
    km = float(km.replace(",", "."))
    miles = km * 0.621371

    print("{0} kilometers is {1} miles.".format(km, miles))

    a = input("Convert some more yes/no: ")
    if a == "no":
        print("Goodbye")
        break