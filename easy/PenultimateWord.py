#CodeEval Penultimate Word

#https://www.codeeval.com/open_challenges/92/submit/

test_cases = ["some line with text",
              "another line"]
for test in test_cases:
    print(test.split(" ")[-2])
