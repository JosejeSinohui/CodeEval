#Code Eval - findASquare
#https://www.codeeval.com/open_challenges/101/

test_cases = ["(1,6), (6,7), (2,7), (9,1)",
              "(4,1), (3,4), (0,5), (1,2)",
              "(4,6), (5,5), (5,6), (4,5)",
              "(4,2), (4,1), (3,7), (6,4)"]

def distance(a,b):
    x1 = int(a[1])
    y1 = int(a[3])
    x2 = int(b[1])
    y2 = int(b[3])
    return ((x2-x1)**(2)+(y2-y1)**(2))**(.5)



for test in test_cases:
    test = test.split(", ")
    distancias = []
    for i in range(len(test)):
        for j in range(i+1,len(test)):
            distancias.append(distance(test[i],test[j]))

    
    a = 0
    lado = 0
    lados = False
    diagonales = False
    for i in range(len(distancias)):        
        for j in range(i+1,len(distancias)):
            if lados == True:
                break
            if a == 4:
                if distancias.count(distancias[i])==4:
                    lado = distancias[i]
                    lados = True
                    break
               
            
            if distancias[j] == distancias[i]:
                a = a + 1
                
            
    if diagonales == False:
        for i in range(len(distancias)):        
            for j in range(i+1,len(distancias)):
                if diagonales == True:
                    break
                if distancias[j] == distancias[i] and distancias[j]!=lado:
                    diagonales = True
                    break
              
                
    if (diagonales and lados):
        print("true")

    else:
        print("false")
    
                   

                    
            
        
            

