test_cases = [2,10,67]

for test in test_cases:
    num = ""
    while(test>0):
        a = test
        b = test//2
        if b == 0:
            num = num + "1"
            break
        num = num + str(a%b)
        test = b
    print(num)
