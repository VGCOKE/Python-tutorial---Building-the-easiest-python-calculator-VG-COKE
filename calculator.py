print("Calculator | VG COKE") #title (optional)
def cal(): #create a function
    num1 = int(input("Type in the first number: ")) #input number #int=integer
    num2 = int(input("Type in the second number: ")) #input number #int=integer #2nd number
    print("1- plus, 2- minus, 3- times, 3- divide") #print out the options
    option = input("Type in the option: ")#input option
    if option =="1":
        print(num1, "+", num2, "=", num1 + num2)
    if option =="2":
        print(num1, "-", num2, "=", num1 - num2)
    if option =="3":
        print(num1, "x", num2, "=", num1 * num2)
    if option =="4":
        print(num1, "/", num2, "=", num1 / num2)
    else:
        print("ERROR, invalid option!")
        cal()
cal()