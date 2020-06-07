print("Hello, Wellcome to my Python besic calculator\n\n")
 #The purpose of this project is to implement a very besic calculator using the if statement to determine the conditions


Num1 = float(input("Enter a the first number: "))
operator = input("Enter an operator ")
Num2 = float(input("Enter a the second number: "))

# We have to set some conditions for operator
if operator=="+":
    print("The sum of two number is : ")
    result = Num1 + Num2
    print(result)
    input(print("Press Any key to continue...."))
elif operator=="-":
    print("The difference of two number is : ")
    result = Num1 - Num2
    print(result)
    input(print("Press Any key to continue...."))
elif operator=="*":
    print("The multiplication of the two number is : ")
    result = Num1 * Num2
    print(result)
    input(print("Press Any key to continue...."))
elif operator=="/":
    if Num2 <= 0:
        print("Cant divide by zero!!")
        exit(0)
        input(print("Press Any key to continue...."))
    print("The division of the two number is : ")
    result = Num1 / Num2
    print(result)
    input(print("Press Any key to continue...."))
elif operator=="%":
    print("The remainder of the two number is : ")
    result = Num1 % Num2
    print(result)
    input(print("Press Any key to continue...."))
else:
    print("Invalid operator selection...!")
    input(print("Press Any key to continue...."))

