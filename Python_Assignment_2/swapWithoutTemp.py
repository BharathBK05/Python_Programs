class swapWithoutTemp():
    def swap(self, val_1,val_2):
        val_1,val_2 = val_2, val_1
        print("After Swapping")
        print("Value 1 = " + str(val_1))
        print("Value 2 = " + str(val_2))

val_1 = int(input("Enter the Value 1 : "))
val_2 = int(input("Enter the Value 2 : "))
print("Before Swapping")
print("Value 1 = " + str(val_1))
print("Value 2 = " + str(val_2))
obj = swapWithoutTemp()   
obj.swap(val_1,val_2)     