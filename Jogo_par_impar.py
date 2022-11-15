def jogo_par_impar():
    import random
    import time

    print('BEM VINDO AO JOGO DE PAR OU ÍMPAR!!!')
    jogadas = int(input('Seleciona como você deseja jogar\n'
            '[1] - Tenta a sorte - 1 tentativa\n'
            '[2] - Melhor de 3\n'
            '[3] - Melhor de 5\n'))
    soma = 0
    escolha_pc = 0
    contador_user = 0
    contador_pc = 0 

    if jogadas == 1:
        jogadas = 0
        escolha_user = int(input('Digite o seu número entre 1 e 10: '))
        if escolha_user % 2  == 0:
            print('Você escolheu PAR\n')
            print('Certo!!! IMPAR!!!!!!\n')
            escolha_pc = random.randrange(1,10,2)
            time.sleep(2)
            print('Eu escolhi: ', escolha_pc)
            soma = escolha_user + escolha_pc
            if soma % 2 == 0:
                print('A soma é par, você ganhou a rodada!!')
                contador_user += 1
                print(f'Você {contador_user} x PC {contador_pc}')
            else:
                print('A soma é impar, você perdeu!!')
                contador_pc += 1
                print(f'Você {contador_user} x PC {contador_pc}')
        else:
            print('Você escolheu IMPAR\n')
            print('Certo! PAR!!!!!!!!')
            escolha_pc = random.randrange(0,11, 2)
            time.sleep(2)
            print('Minha escolha: ',escolha_pc)
            soma = escolha_user + escolha_pc
            if soma % 2 == 0:
                print('A soma é par, você perdeu')
                contador_pc += 1
                print(f'Você {contador_user} x PC {contador_pc}')
            else:
                print('A soma é impar, você ganhou!!!')
                contador_user += 1
                print(f'Você {contador_user} x PC {contador_pc}')
        print('Fim do Jogo')

    if jogadas == 2:
        while True:
            if contador_pc >= 2 or contador_user >= 2:
                break
            escolha_user = int(input('Digite o seu número entre 1 e 10: '))
            if escolha_user % 2 == 0:
                print('Você escolheu um numero PAR!\n'
                    'Certo, IMPAR!!!!!')
                escolha_pc = random.randrange(1,10,2)
                time.sleep(2)
                print('Eu escolho: ', escolha_pc)
                soma = escolha_pc + escolha_user
                if soma % 2 == 0:
                    print(f'A soma é {soma}. Você acertou!')
                    contador_user += 1
                    print(f'Você: {contador_user} x  PC: {contador_pc}')
                else:
                    print(f'A soma é {soma}. Você perdeu!!')
                    contador_pc += 1
                    print(f'Você: {contador_user} x PC: {contador_pc}')
            else:
                print('Você escolheu um número IMPAR!!\n'
                    'Certo!!! PAR!!!!!!')
                escolha_pc = random.randrange(0,11, 2)
                time.sleep(2)
                print('Eu escolho: ', escolha_pc)
                soma = escolha_pc + escolha_user
                if soma % 2 == 0:
                    print(f'A soma é de {soma}. Você perdeu!!')
                    contador_pc += 1
                    print(f'Você: {contador_user} x PC: {contador_pc}')
                else:
                    print(f'A soma é {soma}. Você ganhou!!')
                    contador_user += 1
                    print(f'Você: {contador_user} x PC: {contador_pc}')

    if jogadas == 3:
        while True:
            if contador_pc >= 3 or contador_user >= 3:
                break
            escolha_user = int(input('Digite o seu número entre 1 e 10: '))
            if escolha_user % 2 == 0:
                print('Você escolheu um numero PAR!\n'
                    'Certo, IMPAR!!!!!')
                escolha_pc = random.randrange(1,10,2)
                time.sleep(2)
                print('Eu escolho: ', escolha_pc)
                soma = escolha_pc + escolha_user
                if soma % 2 == 0:
                    print(f'A soma é {soma}. Você acertou!')
                    contador_user += 1
                    print(f'Você: {contador_user} x  PC: {contador_pc}')
                else:
                    print(f'A soma é {soma}. Você perdeu!!')
                    contador_pc += 1
                    print(f'Você: {contador_user} x PC: {contador_pc}')
            else:
                print('Você escolheu um número IMPAR!!\n'
                    'Certo!!! PAR!!!!!!')
                escolha_pc = random.randrange(0,11, 2)
                time.sleep(2)
                print('Eu escolho: ', escolha_pc)
                soma = escolha_pc + escolha_user
                if soma % 2 == 0:
                    print(f'A soma é de {soma}. Você perdeu!!')
                    contador_pc += 1
                    print(f'Você: {contador_user} x PC: {contador_pc}')
                else:
                    print(f'A soma é {soma}. Você ganhou!!')
                    contador_user += 1
                    print(f'Você: {contador_user} x PC: {contador_pc}')
        

    print('Fim de jogo\n'
        f'Placar final: Você: {contador_user} x PC: {contador_pc}')

    jogar_novamente = str(input('Deseja jogar novamente? [S/N]')).upper()
    if jogar_novamente == 'S':
     return(jogo_par_impar())
    else:
        exit

jogo_par_impar()

