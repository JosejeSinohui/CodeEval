#CodeEval -DataRecovery
#https://www.codeeval.com/open_challenges/140/
test_cases = ["2000 and was not However, implemented 1998 it until;9 8 3 4 1 5 7 2",
              "programming first The language;3 2 1",                      
              "programs Manchester The written ran Mark 1952 1 in Autocode from;6 2 1 7 5 3 11 4 8 9"]
for test in test_cases:
    #inicializa oracion
    oracion = ""
    
    #separa la oracion de los numeros
    test = test.split(";") 
    
    #separa las palabras de la oracion"
    palabras = test[0].split(" ") 
    
    #separa los numeros de la oracion
    #remueve newline del ultimo elemento (CodeEval los manda asi)
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

