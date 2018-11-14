import re


class Postfix:

    @staticmethod
    def main(inp):  # Main function in class
        parse = Postfix.parsing(inp)
        return parse

    @classmethod
    def parsing(cls, inp):  # Parsing user input to postfix notation

        try:
            string = list(inp.replace(" ", ""))
            output = list()
            oper_stack = list()
            i = 0
            pre = ""

            while i < len(string):  # While there are elements in string

                if string[i] == "+":
                    try:
                        if re.match("[()]", string[i-1]) or string.index(string[i]) == 0:
                            pre = "+"
                            i += 1
                            continue
                    except IndexError:
                        pre = "+"
                        i += 1
                        continue

                if string[i] == "-":
                    try:
                        if re.match("[()]", string[i-1]) or string.index(string[i]) == 0:
                            pre = "-"
                            i += 1
                            continue
                    except IndexError:
                        pre = "-"
                        i += 1
                        continue

                if re.match("[\d.]", string[i]):
                    # If the integer
                    f = ""
                    while re.match("[\d.]", string[i]):
                        f += string[i]
                        i += 1
                        if i == len(string):
                            break
                    i -= 1
                    output.append(pre + f)
                    pre = ""

                if re.match("!", string[i]):
                    # If the postfix operator
                    output.append(string[i])

                if re.match("[a-z]", string[i]):
                    # If the prefix function
                    f = ""
                    while re.match("[a-z]", string[i]):
                        f += string[i]
                        i += 1
                        if i == len(string):
                            break
                    i -= 1
                    oper_stack.append(f)

                if string[i] == "(":
                    # If the "("
                    oper_stack.append(string[i])

                if string[i] == ")":
                    # If the ")"
                    s = oper_stack.pop()
                    while s != "(":
                        output.append(s)
                        s = oper_stack.pop()

                if re.match("[+\-/*^]", string[i]):
                    # If the operator
                    if oper_stack:
                        if Postfix.get_priority(oper_stack[-1]) >= Postfix.get_priority(string[i]):
                            output.append(oper_stack.pop())
                    oper_stack.append(string[i])

                i += 1

            while len(oper_stack) > 0:
                output.append(oper_stack.pop())

            return output

        except Exception:
            exit("Something broken or may you entered invalid expression")

    @classmethod
    def get_priority(cls, c):  # Getting priority of operators
        if c == "(":
            return 0
        elif c == ")":
            return 1
        elif c == "+":
            return 2
        elif c == "-":
            return 2
        elif c == "*":
            return 3
        elif c == "/":
            return 3
        elif c == "^":
            return 4
        else:
            return 5
