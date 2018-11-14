import re


class Error:

    @staticmethod
    def check_input(inp):
        string = inp

        if len(string) == 0:
            exit("Your input must contain something")

        if string.count("(") != string.count(")"):
            exit("SyntaxError: Unpaired bracket")

        if re.search("[+\-*/^]{2,}", string):
            exit("SyntaxError: Few operators near")

        if re.search("[^\da-z.+\-*/^!() ]", string):
            exit("SyntaxError: Invalid character")

        if re.search("[+\-*/^]!", string):
            exit("SyntaxError: Invalid expression")

    @staticmethod
    def check_postfix(inp):
        string = inp

        for i in string:
            if re.match("[a-z]+", i) and not re.match("sin|cos|tan|tg|ctg|abs|root", i):
                exit("Unknown function")
