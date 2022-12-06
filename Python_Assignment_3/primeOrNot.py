class primeOrNot():
    def check(self, input):
        try:
            if input > 1:
                flag = 0
                for i in range(2,int(input/2) + 1):
                    if input%i == 0:
                        flag = 1
                        break
                    else:
                        flag = 0
                        
                return flag     
            else:
                return -1  
        except Exception as e:
            print(e)       

if __name__ == '__main__':
    input = int(input("Enter the Value : "))
    obj = primeOrNot()   
    flag = obj.check(input)   
    if flag == 1:
        print("The Number " + str(input) + " is not prime")   
    elif flag == 0:
        print("The Number " + str(input) + " is prime")
    else:
        print("The number is less than 1")  


