import sys

def helloWorld(string1, string2):
    if not string1 and not string2:
        print("None is provided")
    elif not string1:
        print(f"String1 is missing, but String2 is: {string2}")
    elif not string2:
        print(f"String2 is missing, but String1 is: {string1}")
    else:
        print(f"{string1} {string2}")

if __name__ == "__main__":
    string1 = sys.argv[1] if len(sys.argv) > 1 else None
    string2 = sys.argv[2] if len(sys.argv) > 2 else None
    helloWorld(string1, string2)