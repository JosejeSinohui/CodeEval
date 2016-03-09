#CodeEval -DataRecovery
#https://www.codeeval.com/open_challenges/140/
test_cases = ["early FLOW-MATIC in programming Hopper was US, language devised Grace the called Another by;2 14 10 3 9 5 12 4 6 8 11 13 1\n",
              "Autocode the early Alick At the developed 1950s Manchester, Glennie University in of;9 11 12 6 1 2 8 13 5 7 3 10\n",
              "expressions mathematical in form code, Short understandable machine statements Code Unlike represented;9 8 10 12 3 4 11 2 6 5 1\n",
              "code time However, program to the be process into had ran, it making translated than every equivalent running slower the the machine code much machine;10 12 1 3 5 22 6 17 8 4 14 13 15 7 20 11 23 21 19 2 16 24 25 18\n",
              "AIMACO it at were was direct major COBOL, time since in descendent its the design only actual in influence and a of use Flow-Matic the;18 13 23 19 2 16 4 10 25 11 6 17 15 7 8 12 21 20 5 14 3 9 22 1\n",
              "and available publicly complete was became in early substantially 1958 The compiler 1959 in FLOW-MATIC;10 6 5 13 11 4 14 8 12 9 1 3 15 7\n",
              'autocode developed The Mark called by 1 was Brooker for the 1954 was second Autocode" the 1 and "Mark in;3 5 1 8 16 10 9 4 11 6 7 13 15 2 20 17 19 14 18\n',
              "implemented However, until 2000 not and was it 1998;5 1 6 9 4 8 3 2",]
for test in test_cases:
    #inicializa oracion
    oracion = ""
    
    #separa la oracion de los numeros
    test = test.split(";") 
    
    #separa las palabras de la oracion"
    palabras = test[0].split(" ") 
    
    #separa los numeros de la oracion
    #remueve newline del ultimo elemento
    numeros = test[1].split(" ")
    numeros[-1] = numeros[-1].strip()
    
    #genera la oracion
    for i in range(len(palabras)):
        if str(i+1) in numeros:
            palabra = palabras[numeros.index(str(i+1))]
        else:
            palabra = palabras[-1]
        oracion = oracion + palabra +" "
        
    print(oracion)

