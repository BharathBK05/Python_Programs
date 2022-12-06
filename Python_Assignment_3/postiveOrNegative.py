class postiveOrNegative():
    def check(self, input):
        if input > 0:
            print("The Number " + str(input) + " is Positive")
        elif input < 0:
            print("The Number " + str(input) + " is Negative")   
        else:
            print("The Number is Zero")

if __name__ == '__main__':
    input = int(input("Enter the Value : "))
    obj = postiveOrNegative()   
    obj.check(input)     