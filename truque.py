lista1 = ['A1','A2','A3','A4','A5','A6','A7']
lista2 = ['B1','B2','B3','B4','B5','B6','B7']
lista3 = ['C1','C2','C3','C4','C5','C6','C7']
print("Olá, seja bem vindo!\n Vamos começar?")
print("")
print("O jogo consiste em você escolher uma das cartas e informar em qual coluna está a carta, e o computador irá embaralhar as cartas,\ne você terá que escolher novamente uma coluna, e assim sucessivamente por 3 vezes\nNo final da terceira rodada o sistema irá te informar, qual foi sua carta!.")
print("Vamos começar!")
print("")
rodada = 0
while rodada < 3:
    rodadaprint=rodada
    print(f"####### rodada nº {rodadaprint+1}##########")
    print("A  B  C")
    for i in range(0,7):
        print(lista1[i],lista2[i],lista3[i])
    opcao = input("Escolha uma das colunas: ")
    if opcao == 'A' or opcao == 'a':
        juncao = lista2+lista1+lista3
    elif opcao == 'B' or opcao == 'b':\
        juncao = lista1+lista2+lista3
    else:
        juncao = lista1+lista3+lista2
    n = 3
    juncao = [juncao[i::n] for i in range(3)]
    lista1 = juncao[0]
    lista2 = juncao[1]
    lista3 = juncao[2]
    rodada += 1
resultado = lista1+lista2+lista3
print(f'Você escolheu > {resultado[10]} <, certo?')
resp = input("Sim ou Não? ")
if resp == 'Sim' or resp == 'sim':
    print("\033[32;7mEu sou o melhor!")
else:
    print("\033[31;7mVocê é burro ao ponto de não saber decorar a própria escolha!")