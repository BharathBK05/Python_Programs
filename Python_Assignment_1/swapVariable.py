class swapVariable():
    def swap(self,var_1,var_2):
        temp = var_1
        var_1 = var_2
        var_2 = temp
        print("After Swap")
        print("variable 1 = " + str(var_1))
        print("variable 2 = " + str(var_2))

obj = swapVariable()
var_1 = int(input("value 1 = "))
var_2 = int(input("value 2 = "))
print("Before Swap")
print("variable 1 = " + str(var_1))
print("variable 2 = " + str(var_2))
obj.swap(var_1,var_2)
 
