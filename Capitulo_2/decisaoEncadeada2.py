nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_infectocontagiosa = input("Suspeita de doenca infectocontagiosa ? ").upper()

# PRIMEIRO PROBLEMA A SER RESOLVIDO
if doenca_infectocontagiosa == "SIM":
    print("Encaminhe o paciente para a sala AMARELA")
elif doenca_infectocontagiosa == "NAO":
    print("Encaminhe o paciente para a sala BRANCA")
else:
    print("Responda a suspeita de doenca infectocontagiosa com SIM ou NAO")

# SEGUNDO PROBLEMA A SER RESOLVIDO
if idade >= 65:
    print("Paciente COM prioridade")
else:
    genero = input("Digite o genero do paciente: ").upper()
    if genero == "FEMININO" and idade > 10:
        gravidez = input("A paciente esta gravida ? ").upper()
        if gravidez == "SIM":
            print("Paciente COM prioridade")
        else:
            print("Paciente SEM prioridade")
    else:
        print("Paciente SEM prioridade")