count = 0
while(count<10):
    if(count == 5):
        count = count+4
        continue  # executa o If e volta pro começo do looping agora
    count = count + 1
    print(count)

print("----------")

a = "oioioioi"
for i in a:
    if(i=="o"):
        print("a" ,end='')
        continue
    print(i, end='')

print("\n----------")

cont = 0
while (cont<=10):
    print(cont)
    if (cont == 7):
        break  # executa o If e quebra a looping
    cont = cont + 1

print("----------")

cont = 0 
while (cont<100):
    if(cont==4):
        break
    else:
        pass #pass server pra substituir codigo faltante
    cont = cont + 1
    print(cont)