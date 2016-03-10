#CodeEval -FizzBuzz
#https://www.codeeval.com/open_challenges/1/

test_cases = ["3 5 10",
              "2 7 15"] # Test cases come from CodeEval

for test in test_cases:
    sequence = ""
    test = test.split(" ")
    fizz = int(test[0])
    buzz = int(test[1])
    count = int(test[2])
    for i in range(1,count+1):
        if(i%fizz == 0 and i%buzz == 0):
            add = "FB"
        elif(i%fizz == 0):
            add = "F"
        elif(i%buzz == 0):
            add = "B"
        else:
            add = str(i)
        sequence = sequence + add +" "
    print(sequence)
    
