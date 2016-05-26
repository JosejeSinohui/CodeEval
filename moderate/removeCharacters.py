# Code Eval - Remove Characters
# https://www.codeeval.com/open_challenges/13/

test_cases = ["how are you, abc",
              "hello world, def"]
for test in test_cases:
    string = list(test.split(", ")[0])
    characters = test.split(", ")[1].strip()

    for i in characters:
        while i in string:
            string.remove(i)
    print("".join(string))
