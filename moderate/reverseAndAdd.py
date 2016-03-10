#CodeEval Reverse and Add
#https://www.codeeval.com/open_challenges/45/

test = 1955
test = int(test) # Test from codeeval is string
i = 0;
while(True):
    backwardsTest = str(test)[::-1]
    if str(test) == backwardsTest:
        break;
    test = test + int(backwardsTest)
    i = i + 1

print(str(i) + " " + str(test))
    
