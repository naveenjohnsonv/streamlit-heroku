print("Enter the two Number:")
number1=int(input())
number2=int(input())
def Div(number1,number2):
    if number1<number2:
        return 0
    return 1 + Div(number1-number2, number2)
print("result ",Div(number1,number2))
