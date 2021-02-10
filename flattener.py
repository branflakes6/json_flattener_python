import sys
import json


def flatten(inputJSON, outputJSON={}, key_name=''):
    if type(inputJSON) is dict:

        for keys in inputJSON:
            flatten(inputJSON[keys], outputJSON, key_name + keys + '.')

    else:
        key_name = key_name[:-1]
        outputJSON[key_name] = inputJSON

    return outputJSON


def main():
    try:
        if not sys.stdin.isatty():
            obj = json.load(sys.stdin)
            print(obj)

    except Exception:
        print("Input Error")


if __name__ == "__main__":
    main()
