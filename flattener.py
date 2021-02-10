import sys
import json


# flatten is a recursive function that takes in a JSON and outputs a flattened version of the JSON
# inputJSON = JSON file passed in from the command line
# outputJSON = python default value, used to recursively build the flattened json
# key_name = string passed recursively to correctly name keys

def flatten(inputJSON, outputJSON={}, key_name=''):
    if type(inputJSON) is dict:  # check if inputObj is an object, if so we need to go through all its key-value pairs

        for keys in inputJSON:  # loop through all key-value pairs in the object
            flatten(inputJSON[keys], outputJSON, key_name + keys + '.')
            # recursive call, this will flatten any nested objects

    else:  # inputObj is not an object
        key_name = key_name[:-1]  # removes redundant '.' if no more nesting is occurring
        outputJSON[key_name] = inputJSON  # store key value pair in the output json

    return outputJSON


def main():
    try:  # try to get a valid JSON file from the command line
        if not sys.stdin.isatty():
            obj = json.load(sys.stdin)  # file has been inputted, load the json from it
            print(flatten(obj))  # print the result of flattening the file

    except Exception:
        print("Input Error")


if __name__ == "__main__":
    main()
