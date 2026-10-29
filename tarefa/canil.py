#atividade de centro de doação:
arquivo = open("Canil.txt", "a", encoding='utf-8') #.txt le o nome do arquivo como sendo arquivo de texto (string), "a" salva aquilo que você escreveu dentro do arquivo, encoding='utf-8' reconhece textos com acentuação e com ç
nomes = []
racas = []

print("=== CANIL ===")
for i in range (5): 
    nome = input("Digite o nome do cachorro: ")
    nomes.append(nome)
    raca = input("Digite a raça do cachorro: ")
    racas.append(raca)

    arquivo.write (nome + " " + raca + "\n")

arquivo.close()