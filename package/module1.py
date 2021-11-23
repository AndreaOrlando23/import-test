from package.module2 import Module2


class Module1:

    def __str__(self):
        return "Module 1 - It works!"

    def response_from_module2(self):
        response = Module2()
        return response


# TEST
def main():
    test_module1 = Module1()
    print(test_module1)  # output: Module1 - It Works

    test_module2 = test_module1.response_from_module2()
    print(test_module2)  # output: Module2 - It Works


if __name__ == '__main__':
    main()


# use the following command positioned in the root (import-test) to test it out
# >> python3 -m package.module1