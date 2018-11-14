import count
import postfix
import error


class Program:

    @staticmethod
    def main():
        while True:
            i = input("Enter expression:")
            error.Error.check_input(i)

            _postfix = postfix.Postfix.main(i)
            error.Error.check_postfix(_postfix)

            result = count.Count.main(_postfix)
            print("Result: ", result)


Program.main()
