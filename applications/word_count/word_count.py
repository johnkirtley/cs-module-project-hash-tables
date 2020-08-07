def word_count(s):
    # Your code here
    cache = {}
    ignored = '"":;,.-+=/\\|[]{}()*^&'
    new_string = s.lower().replace("\t", " ").replace(
        "\n", " ").replace("\r", " ").split(" ")

    for val in new_string:
        val = val.strip(ignored)

        if val not in cache and val != "":
            cache[val] = 1
        elif val != "":
            cache[val] += 1
    return cache


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
