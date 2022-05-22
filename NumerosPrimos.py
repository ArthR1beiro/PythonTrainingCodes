# calculadore da numeros primos

for i in range(2,30):
    j = 2
    cont = 0
    while (j < i):
        if(i % j == 0):
            cont = 1
            j = j + 1
        else:
            j = j + 1
            
    if (cont == 0):
        print(str(i) + " é um numero primo")
        cont = 0
    else:
        cont = 0