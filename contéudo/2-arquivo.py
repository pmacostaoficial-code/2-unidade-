arquivo = open("pessoal.txt", "w") #USE O "W" PARA RESCREVER O CÓDIGO NO ARQUIVO, USE O "A" PARA SALVAR O TEXTO QUE FOI CRIADO DENTRO DO ARQUIVO, SEM NECESSIDADE DE FICAR ESCREVENDO DE NOVO O TEXTO 

nomes = []
sobrenomes = []
idades = []

for i in range (3):
    nome = input("Digite seu nome: ").upper()
    nomes.append(nome)
    sobrenome = input("Digite o sorbenome: ").upper()
    sobrenomes.append(sobrenome)
    idade = input("Digite a idade: ")
    idades.append(idade)

    arquivo.write(nome + " " + sobrenome + " " + str(idade) + "\n")

arquivo.close()

        
                   
                   

