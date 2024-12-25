from struct import calcsize


def add(first_number,second_number):
    return first_number+second_number

def subtract(first_number, second_number):
    return first_number-second_number

def multiply(first_number, second_number):
    return first_number*second_number

def divide(first_number, second_number):
    return first_number/second_number


operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

def caluculator():
    should_accumalate = True
    num1 = float(input("pick a number\n"))
    while should_accumalate:
        for symbol in operations:
            print (symbol)
        operation_symbol = input("pick an operation\n")
        num2 = float(input("pick a number\n"))
        result = (operations[operation_symbol](num1,num2))
        print(f"{num1}{operation_symbol}{num2} = {result} ")

        choice = input(f"Pick Y  if would you like to continue calculating with {result} or type N to stop\n")
        if choice == "Y":
            num1 = result
        else:
            should_accumalate = False
            print("\n"*20)
            print(f"{num1}{operation_symbol}{num2} = {result} ")
            caluculator()
caluculator()
# replay = True
# if not replay:
#     first_number = int(input("pick a number\n"))
#     print("+","-","*","/")
#     operation = input("pick an operation\n")
#     second_number = int(input("pick a number\n"))
#
#     result = operations[operation](first_number,second_number)
#     print = result
#     else:
#     first_number = result
#

# result = (f"{first_number} {operation} {second_number}")
# print(result)

# try_again = True:
#
# if replay == "n"
#     try_again = False
#     print(final_calculation)
#     return
#while try_again:





