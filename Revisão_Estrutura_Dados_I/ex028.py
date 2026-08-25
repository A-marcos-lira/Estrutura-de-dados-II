from random import randint
from time import sleep #Faz o computador esperar por alguns segundos
computador= randint(0,5) #Faz o computador "PENSAR"
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
usuario = int(input('Em que número eu pensei? ')) #Usuário (Jogador) tenta adivinhar
print('PROCESSANDO...')
sleep(2) #Quanto tempo o computador esperar
if usuario == computador:
    print('PARABÉNS!! Você conseguiu me vencer!')
    print('O número era {}'.format(computador))
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, usuario))
print('=====FIM DO JOGO=====')