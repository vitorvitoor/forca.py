import os;
import sys;

def boas_vindas():
    print('Bem-vindo ao Jogo da Forca!')

def limpar_tela():
    os.system("cls")

def continuar():
    os.system("pause")
 
def mostrar_palavra(palavra, chutes):
    for i in range(len(palavra)): 
        if (palavra[i] in chutes):
            sys.stdout.write(palavra[i])
        else: 
            sys.stdout.write('_')
        sys.stdout.write(' ')


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print('Cabeça!')

    if(erros == 2):
        print('Braços direito!')

    if(erros == 3):
        print('Braço esquerdo!')

    if(erros == 4):
        print('Perna direita!')

    if(erros == 5):
        print('Perna esquerda!')

    

    print(" |            ")
    print("_|___         ")
    print()
    
def ganhou():
    print("Parabéns, você ganhou!")
    return

def perdeu(palavra):
    print('Ops, você foi enforcado!')
    print("A palavra chave era {}".format(palavra))
