class kmToMiles():
    def __init__(self, km):
        print("Miles = " + str(km * 0.62137119))

km = int(input("Enter the KM : "))
obj = kmToMiles(km)        