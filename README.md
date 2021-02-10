# json_flattener_python
# Problem Description
Write a program that takes a JSON object as input and outputs a flattened version of the JSON object, with keys as the path to every terminal value in the JSON structure. Output should be valid JSON.

For example, consider the following JSON object:
```
{
    "a": 1,
    "b": true,
    "c": {
        "d": 3,
        "e": "test"
    }
}
```
In this example the path to the terminal value 1 is "a" and the path to the terminal value 3 is "c.d".

The output for the above object would be:
```
{
    "a": 1,
    "b": true,
    "c.d": 3,
    "c.e": "test"
}
```

# Assumptions
- The input you receive will be a JSON object
- All keys named in the original object will be simple strings without ‘.’ characters
- The input JSON will not contain arrays
- You may use a library to parse JSON from a string to an object
- Command line should correspond to linux conventions, eg using pipes cat test.json | mycode
- Your code will be judged on correctness and code quality, but you do not need to focus on performance optimizations
-Please add tests to validate that your code works correctly.

# Overview
I chose to use Python to tackle this problem for two reasons:

1. I was aware that Python has many built in tools for processing and parsing JSON Objects, the Python Dictionaries are equivelant to
JSON objects and can be used to easily manipulate data within a JSON.

2. The second reason I decided to use Python was purely personal, I have used Python a little bit in the past
but I was looking to further my knowledge and this seemed like a good opportunity to learn something practical.


# Approach
## Flatten Function

My flatten function is a recursive approach to the problem, this seemed like the most obvious solution to me as it needs to
handle jsons of unknown length and complexity. This algorithm checks if the type of the input is a Python dictionary, if it is then we have some nesting to resolve
otherwise we can just add the key-value pair to our output JSON. If we have a dict type then we need to recursively go through it building out the key_name until 
we hit the terminal value.

Originally flatten was done just using a default empty value for the output JSON but during testing I discovered some issues with this.
I am not sure exactly causes the issue but during testing the default value of outputJSON was not being used, instead the tests would pass
the result of the last test in as outputJSON causing the result to be incorrect. To solve this I added a function that calls the recursive function with an empty output json.

This algorithm runs in O(n) time.

## File Input

File input is done via std.in using linux pipes. The main takes in a valid json file and uses json.load to parse the json
to a Python Dict. This is then passed into the flatten function, one of potential issues with json.load is it does not preserve the order
of the json object. I don't know if this matters to the problem as you can still access all the keys, if it does it can be fixed by importing
OrderedDict and changing: 
```
obj = json.load(sys.stdin)
```

to:
```
obj = json.load(sys.stdin, object_pairs_hook=OrderedDict)
```

## Testing

Testing is done via Python unittest. The following tests all run correctly:
- Test Empty: Tests for an empty JSON
- Test Flatten: Tests the example JSON
- Test Flatten Nesting: Tests JSONS with a lost of nesting
- Test Already Flat: Tests an already flattened JSON
- Test Duplicate Key: Tests a JSON with a duplicate key

I also tested piping files via Linux pipes following the format in the problem description 

```
cat test.json | python flatener.py
```

# Time Spent & Road Blocks

I spent about 3 hours on this challenge. Most of this was spent on learning various things about Python, JSONS and file handling
that I did not know beforehand. I have only done a few small Python projects so I had never handled files or written tests in Python,
I spent about 30 minutes learning about linux pipes and how to pass a JSON file into a Python script which is how I learned that
json.load does not preserve the ordering of the JSON. 

I spent about 30 minutes writing the flatten function which required me to brush up on my knowledge of Python and learn about Dictionaries.

I spent about an hour writing tests due to a roadblock outlined in the testing section where I encountered a bug with Python default values.

The rest of my time was spent improving my code, reading information relevant to the challenge and writing the README.