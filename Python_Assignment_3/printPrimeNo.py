class primeOrNot():
    def check(self, start,end):
        try:
            for i in range(start,end+1):
                if i == 1:
                    continue
                
                flag = 1
                for j in range(2,int(i/2) + 1):
                    if i%j == 0:
                        flag = 0
                        break

                if flag == 1:
                    print(i,end = ' ')           
                 
        except Exception as e:
            print(e)       

if __name__ == '__main__':
    start = int(input("Enter the start value : "))
    end = int(input("Enter the end value : "))
    obj = primeOrNot()   
    flag = obj.check(start,end)    


