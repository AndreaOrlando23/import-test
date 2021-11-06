from package.module1 import Module1


def main():
    test_module1 = Module1()
    print(test_module1)
    
    test_module2 = test_module1.response_from_module2()
    print(test_module2)


if __name__ == '__main__':
    main()


"""
Output da Visual Studio Code:
Traceback (most recent call last):
  File "/Users/utente/Desktop/TomorrowDevs/import_test/main.py", line 1, in <module>
    from package.module1 import Module1
ImportError: No module named package.module1


Output da Terminal:
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    from package.module1 import Module1
  File "/Users/utente/Desktop/TomorrowDevs/import_test/package/module1.py", line 1, in <module>
    from module2 import Module2
ModuleNotFoundError: No module named 'module2'
"""