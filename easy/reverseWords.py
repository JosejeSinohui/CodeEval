#Code Eval Reverse Words
#https://www.codeeval.com/open_challenges/8/submit/?lid=1410765


test_cases = ["Hello World",
              "Hello CodeEval"]
for test in test_cases:
    test = test.split(" ")
    test[-1] = test[-1].strip()
    print(" ".join(test[::-1]))
    
    

