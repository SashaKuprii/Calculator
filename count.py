import re
import math
# from sympy import *


class Count:

    @staticmethod
    def main(inp):
        result = Count.counting(inp)
        return result

    @classmethod
    def counting(cls, inp):
        try:
            string = inp
            stack = list()
            i = 0
            while i < len(string):

                if re.match("\+?-?\d*.?\d+", string[i]):
                    # If the number
                    stack.append(string[i])

                if re.match("!", string[i]):
                    # If the postfix operator
                    r = 0
                    a = int(stack.pop())

                    if string[i] == "!":
                        r = math.factorial(a)

                    stack.append(r)

                if re.match("sin|cos|tan|tg|ctg|root|abs", string[i]):
                    # If the prefix operator
                    r = 0
                    a = int(stack.pop())

                    if string[i] == "sin":
                        r = math.sin(a)
                    elif string[i] == "cos":
                        r = math.cos(a)
                    elif string[i] == "tan" or string[i] == "tg":
                        r = math.tan(a)
                    elif string[i] == "abs":
                        r = abs(a)
                    elif string[i] == "ctg":
                        r = 1/math.tan(a)
                    elif re.match("root", string[i]):
                        b = int(stack.pop())
                        r = a ** (1 / b)

                    stack.append(r)

                if re.match("^[+\-/*^]$", string[i]):
                    # If the the operator
                    r = 0
                    b, a = int(stack.pop()), int(stack.pop())

                    if string[i] == "+":
                        r = a + b
                    elif string[i] == "-":
                        r = a - b
                    elif string[i] == "*":
                        r = a * b
                    elif string[i] == "/":
                        r = a / b
                    elif string[i] == "^":
                        r = a ** b

                    stack.append(r)
                i += 1

            return stack[0]

        except Exception:
            exit("Something broken or may you entered invalid expression")
