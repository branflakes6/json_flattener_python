import sys
import json


def main():
    try:
        if not sys.stdin.isatty():
            obj = json.load(sys.stdin)
            print(obj)

    except Exception:
        print("Input Error")


if __name__ == "__main__":
    main()
