#Projeto de Gabriel Holthausen RA 1132030 e Vitor Almeida Machado RA 1133554

from atalhos import boas_vindas, limpar_tela, continuar, mostrar_palavra, desenha_forca, ganhou, perdeu

dicas = list
palavra_chave = list
chutes = list
erros = int
acertos = int
mensagem = str
desafiante = str
competidor = str
perdedor = str
vencedor = str
enforca = int


def main():
    global desafiante, competidor, perdedor, vencedor, enforca

    def start_game():
        global dicas, palavra_chave, chutes, erros, acertos, mensagem, desafiante, competidor, perdedor, vencedor, enforca

        dicas = []
        palavra_chave = []
        chutes = []
        erros = 5
        acertos = 0
        mensagem = ''
        desafiante = ''
        competidor = ''
        perdedor = ''
        vencedor = ''
        enforca = 0

    def palpitar():
        global erros, acertos, mensagem, enforca
        palpite = str(input('Digite uma letra ou uma palavra:').upper())
        if len(palpite) > 1:
            if palpite == ''.join(palavra_chave):
                acertos = len(palavra_chave)
                return
            else:
                mensagem = '{} não é a palavra correta.'.format(palpite)
                erros -= 1
                enforca += 1
                return
        if palpite in chutes:
            mensagem = 'Você ja chutou essa letra'
            return
        else:
            chutes.append(palpite)

        if palpite in palavra_chave:
            acertos += 1
            mensagem = 'A letra {} faz parte da palavra!'.format(palpite.upper())
        else:
            erros -= 1
            enforca += 1
            mensagem = 'A letra {} não faz parte da palavra!'.format(palpite.upper())
        print('\n')
            

    
    start_game()
    limpar_tela()
    boas_vindas()

    desafiante = str(input('Digite o nome do desafiante:'));
    competidor = str(input('Digite o nome do competidor:'));

    if len(desafiante) and len(competidor) >= 3: 
        limpar_tela();

        palavra_chave = list(str(input('Digite a palavra chave:').upper()));
        
        while len(palavra_chave) < 3:
            palavra_chave = list(str(input('Palavra chave deve conter no mínimo 3 caracteres:').upper()));
        
        dicas.append(str(input('Primeira dica:').upper()));
        dicas.append(str(input('Segunda dica:').upper()));
        dicas.append(str(input('Terceira dica:').upper()));

        limpar_tela()
        while acertos < len(palavra_chave) and erros > 0:

            print('{}'.format(mensagem));
            desenha_forca(enforca);
            mostrar_palavra(palavra_chave, chutes);
            print('\nAcertos:{}'.format(acertos));
            print('Chances restantes:{}'.format(erros));
            print('(1) Para jogar');
            print('(2) Para receber uma dica');
            opcao = int

            try:
                opcao = int(input('Sua opção:'))
                if opcao == 1:
                    limpar_tela()
                    palpitar()
                elif opcao == 2:
                    if len(dicas) > 0:
                        limpar_tela()
                        print(dicas[0])
                        dicas.pop(0)
                    if len(dicas) > 0:
                        print('Você so tem mais {} dicas'.format(len(dicas)))
                    else:
                        print('Você não tem mais dicas!')
                    palpitar()
            except:
                limpar_tela()
                print('Opção invalida!')
            limpar_tela()

        if erros == 0:
            perdedor = 'Competidor ' + competidor.capitalize()
            vencedor = 'Desafiante ' + desafiante.capitalize()
            perdeu(palavra_chave)

        elif acertos == len(palavra_chave):
            perdedor = 'Desafiante ' + desafiante.capitalize()
            vencedor = 'Competidor ' + competidor.capitalize()
            ganhou()

        w = open('historico.txt', 'a')
        w.write('Palavra: {} - Vencedor: {}, Perdedor: {}\n'.format(''.join(palavra_chave).capitalize(), vencedor, perdedor))
        w.close()
        r = open('historico.txt', 'r')
        print('Historico de partidas')
        print(r.read())
        continuar()
        print('Digite 1 para jogar novamente')
        print('Digite 2 para sair do jogo\n')
        quit_game = int
        while quit_game != 1 or quit_game != 2: 
            try:
                quit_game = int(input('Sua opção:'))
                if quit_game == 1:
                    main()
                elif quit_game == 2:
                    break
            except:
                limpar_tela()
                print('Opção invalida')
    else:
        print("Nomes inválidos!")
        continuar()
        main()



main()