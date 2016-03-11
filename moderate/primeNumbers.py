#Code Eval - Prime Numbers
#https://www.codeeval.com/open_challenges/46/

test_cases = ["10","20","100000"]
def isPrime(n):
    if n < 2:
        return False
    prime = True
    cont = n//2
    while(prime and cont>1):
        if n % cont == 0:
            prime = False
            break
        cont = cont - 1

    return prime

for test in test_cases:
    finished = ""
    for i in range(int(test)):
        if isPrime(i):
            finished = finished + str(i)+","

    print(finished[:-1])
