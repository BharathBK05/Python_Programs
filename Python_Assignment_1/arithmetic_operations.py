class arithmeticOperations():
    def add(self,val1,val2):
        print("Sum = " + str(val1 + val2))

    def division(self,val1,val2):
        try:
            print("Division = " + str(val1/val2))
        except Exception as e:
            print("Error " + str(e))


obj = arithmeticOperations()
val1 = int(input("Value 1 = "))
val2 = int(input("Value 2 = "))
operation = int(input("Enter the Operation to be performed \n 1.Addition \n 2.Division \n "))
if operation == 1:
    obj.add(val1,val2)
elif operation == 2:    
    obj.division(val1,val2)
else:
    print("Invalid selection")    
