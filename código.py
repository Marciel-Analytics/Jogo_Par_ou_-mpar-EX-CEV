import random
computador = random.randint(0,10)
jogador = 0
opcao = 'PI'
cont = 0
print('-'*70)
print("--- VAMOS JOGAR PAR OU ÍMPAR ---")
print('-'*70)
while True:
    jogador = int(input('Escolha um Número: '))
    opcao = str(input('Par ou Impar [P/I]: ')).strip().upper()[0]
    print('-' * 70)
    soma = jogador + computador
    if soma % 2 == 0:
        print(f'você jogou {jogador} e o computador jogou {computador}. TOTAL DE: {soma} DEU PAR')
    else:
        print(f'você jogou {jogador} e o computador jogou {computador}. TOTAL DE: {soma} DEU ÍMPAR')
    print('-' * 70)
    if opcao == 'P' and soma % 2 == 0:
        print('VOCÊ GANHOU')
        print('-' * 70)
        cont += 1
    elif opcao == 'I' and soma % 2 != 0:
        print('VOCÊ GANHOU')
        print('-' * 70)
        cont += 1
    else:
        print('-' * 70)
        print('VOCÊ PERDEU')
        print('-' * 70)
        if cont > 1:
            print(f'GAME OVER!!!   VOCÊ VENCEU {cont} VEZES')
        else:
            print(f'GAME OVER!!!   VOCÊ VENCEU {cont} VEZ')
        print('-' * 70)
        break
