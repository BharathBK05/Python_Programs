class celToFahr():
    def __init__(self, cel):
        print("Fahrenheit = " + str((cel*1.8) + 32))

cel = int(input("Enter the Celcius : "))
obj = celToFahr(cel)        