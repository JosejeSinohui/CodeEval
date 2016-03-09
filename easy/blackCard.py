#codeEval Black Card
#https://www.codeeval.com/browse/222/

test_cases = ["John Sara Tom Susan | 3",
              "John Tom Mary | 5",
              "Vfo Mftmmd Tcc Xnhhh Bmxdp Noyssw Jyssz | 12"]
for test in test_cases:
    names = test.split("|")[0].split(" ")
    number = int(test.split("|")[1])-1
    del names[-1]

    while len(names)!=1:
        i = number
        if len(names)<=number:
            while(i>=len(names)):
                i = i-len(names)
            del names[i]
            continue

        del names[number]
    print(names[0])
