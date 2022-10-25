def solution():
    pass
def solution(num1, num2, op =""):
    if(op == "+"):
        n1 = str(num1)
        n2 = str(num2)
        if not n1.isdigit() and not n2.isdigit():
            return -1
        else:
            calc = num1 + num2
            return calc  
    elif(op == "-"):
        calc = num1 - num2
        return calc
    elif(op == "*"):
        calc = num1 * num2
        return calc
    elif(op == "/"):
        if(num2 == 0):
            return -1
        else:
            calc = num1 / num2
            return calc
    else:
        return -1


