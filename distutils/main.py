# coding=utf-8
import os
import great_module


def main():
    print(great_module.great_function(1))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as err:
        print("KeyboardInterrupt: {0}".format(err))
    except TypeError as err:
        print("TypeError: {0}".format(err))
    except OSError as err:
        print("OS error: {0}".format(err))
    os.system('pause')
