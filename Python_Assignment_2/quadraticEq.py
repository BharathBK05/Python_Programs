import math 

class quadraticEq():

    def equationroots(self,a, b, c): 
    
        dis = b * b - 4 * a * c 
        sqrt_val = math.sqrt(abs(dis)) 
        
        if dis > 0: 
            print(" real and different roots ") 
            print((-b + sqrt_val)/(2 * a)) 
            print((-b - sqrt_val)/(2 * a)) 
        
        elif dis == 0: 
            print(" real and same roots") 
            print(-b / (2 * a)) 
        
        else:
            print("Complex Roots") 
            print(- b / (2 * a), " + i", sqrt_val) 
            print(- b / (2 * a), " - i", sqrt_val) 
  
obj = quadraticEq()
print("Enter the values of the Equation in corresponding format")
print("ax^2+bx+c")  
a = int(input("Enter the a : "))
b = int(input("Enter the b : "))
c = int(input("Enter the c : "))

if a == 0: 
        print("Input correct quadratic equation")  
else:
    obj.equationroots(a, b, c)