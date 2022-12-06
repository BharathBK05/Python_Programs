class leapYear():
    def check(self, input):
        if input%4 == 0:
            if input%100 == 0:
                if input%400 == 0:
                    print("The year " + str(input) + " is a leap year")
                else:
                    print("The year " + str(input) + " is a not leap year")
            else:
                print("The year " + str(input) + " is a leap year")        
        else:
            print("The year " + str(input) + " is a not leap year")   

if __name__ == '__main__':
    input = int(input("Enter the Year : "))
    obj = leapYear()   
    obj.check(input)     