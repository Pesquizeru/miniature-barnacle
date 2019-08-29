arq = open("aaa.txt", "r")
arq.read
lista = list()
for i in arq:
    lista.append(i)
lista.sort()
arq2 = open("bbb.txt", "w")
arq2.writelines(lista)
arq.close()
arq2.close()