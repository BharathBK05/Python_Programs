class oddOrEven():
    def check(self, input):
        if input%2 == 0:
            print("The Number " + str(input) + " is Even")
        else:
            print("The Number " + str(input) + " is Odd")   

if __name__ == '__main__':
    input = int(input("Enter the Value : "))
    obj = oddOrEven()   
    obj.check(input)     