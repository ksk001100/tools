import utils
import sys


if __name__ == '__main__':
    inputs = sys.argv[1:]
    passwords = utils.generate_passwords(inputs)

    for password in passwords:
        print(password)
