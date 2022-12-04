class areaOfTriangle():
    def findArea(self,length,breath):
        print("Area of Triangle = " + str(length * breath))

obj = areaOfTriangle()
length = int(input("Length = "))
breath = int(input("Breath = "))
obj.findArea(length,breath)
 
