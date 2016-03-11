#Code Eval - Trailing String
#https://www.codeeval.com/open_challenges/32/

test_cases = [
              "Hello CodeEval,CodeEval\n",
              "San Francisco Pedro de la cueva,San Francisco Pedro de la cueva"]

for test in test_cases:
    string = test.split(",")[0].lower().split(" ")
    trail = test.split(",")[1].strip().lower().split(" ")

    j = 0
    condition = True
    for i in range(0-len(trail),0):
        if string[i] != trail[j]:
            condition = False
        j = j + 1

    if condition == True:
        print("1")
    else:
        print("0")
