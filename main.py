# coding=utf-8
import os


def main():
    pass


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
