from functools import update_wrapper

#programa que recebe string e retorna a string com cada caracter em maiusculo
#ex: teste
#saida:
#Teste
#tEste
#teSte
#tesTe
#testE

palavra = input("Digite a palavra: ")
palavra = palavra.lower()
l = list(palavra)
for n in range(len(l)):
    l[n] = l[n].upper()
    s = "".join(l)
    l[n] = l[n].lower()
    print(s)