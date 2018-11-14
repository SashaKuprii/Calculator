import postfix


class Program:

    @staticmethod
    def main():
        while True:
            i = input("Enter expression:")
            _postfix = postfix.Postfix.main(i)


Program.main()
