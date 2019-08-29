arq = open("aaa.txt", "r")
arq.read
lista = list()
for i in arq:
    lista.append(i)
arq2 = open("bbb.txt", "r")
arq2.read
for i in arq2:
    lista.append(i)
lista.sort()
print(lista)
arq3 = open("ccc.txt", "w")
arq3.writelines(lista)
arq.close()
arq2.close()