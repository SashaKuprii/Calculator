import count
import postfix


class Program:

    @staticmethod
    def main():
        while True:
            i = input("Enter expression:")

            _postfix = postfix.Postfix.main(i)

            result = count.Count.main(_postfix)
            print("Result: ", result)


Program.main()
