#AULA DE ABRIR ARQUIVO:
arquivo = open("texto.txt", "w") #"a", "w", "r" === aqui você criou o arquivo chamado texto.txt

for i in range (3): #vai repetir oque voc~e vai escrever dentro do arquivo três vezes 
    nome = input("Digite o nome do arquivo: ") #oque você escrever aqui dentro vai abrir no arquivo criado "texto.txt"

    arquivo.write (nome + "\n")