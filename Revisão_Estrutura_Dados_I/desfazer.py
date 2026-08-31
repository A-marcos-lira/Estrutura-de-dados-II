from collections import deque #Importando o deque
#A fia recebe o deque (remoção e inserção)
fila = deque()
#Adicionando elementos dentro da fila
fila.append('Manga')
fila.append('Goiaba')
fila.append('Acerola')
fila.appendleft('Cajú')
#Imprimindo a fila
print(fila)
print('='*50)
#Removendo o ÚLTIMO elemento da direita
remover = fila.pop()
print(remover)
print('='*10)
#Removendo o PRIMEIRO elemento da esquerda
remover = fila.popleft()
print(remover)
print('='*10)
#Imprimindo a NOVA fila com os elementos REMOVIDOS
print(fila)