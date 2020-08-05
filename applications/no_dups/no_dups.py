def no_dups(s):
    # Your code here
    cache = {}
    arr = s.split(" ")
    newString = ""

    for val in arr:
        if val not in cache:
            cache[val] = val

    for val in cache:
        newString += f" {val}"

    return newString.strip()


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
