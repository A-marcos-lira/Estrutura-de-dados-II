#Criando a Classe Paciente
class Paciente:
    def __init__(self, nome, idade, prioridade):
        self.nome = nome
        self.idade = idade
        self.prioridade = prioridade
#Criando a Classe Node
class Node:
    def __init__(self, paciente):
        self.paciente = paciente
        self.proximo = None
#Fila de Atendimento e suas funcionalidades
class FilaAtendimento:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self._tamanho = 0
    #Função para saber se a lista está vazia
    def esta_vazio(self):
        return self.inicio is None

    # Função para saber o tamanho da lista
    def tamanho(self):
        return self._tamanho

    # Adicionando os pacientes conforme a prioridade
    def adicionar(self, paciente):
        novo_no = Node(paciente)
        self._tamanho += 1
        # Condição se a lista está vazia
        if self.esta_vazio():
            self.inicio = novo_no
            self.fim = novo_no
            return
        # Se a prioridade do paciente for "Normal" vai pro final da fila
        if paciente.prioridade == 'Normal':
            self.fim.proximo = novo_no
            self.fim = novo_no

        else:
            if self.inicio.paciente.prioridade == 'Normal':
                novo_no.proximo = self.inicio
                self.inicio = novo_no
            else:
                # Percorre até achar o último paciente com prioridade
                atual = self.inicio
                while atual.proximo and atual.proximo.paciente.prioridade == 'Prioridade':
                    atual = atual.proximo
                # Insere o novo nó logo após o último prioritário
                novo_no.proximo = atual.proximo
                atual.proximo = novo_no

                if novo_no.proximo is None:
                    self.fim = novo_no

    def atender(self):
        if self.esta_vazio():
            print('Nenhum paciente na fila!')
            return None
        # Remove o paciente do início da fila
        paciente_atendido = self.inicio.paciente
        self.inicio = self.inicio.proximo
        self._tamanho -= 1
        # Se a fila esvaziou, o fim também vira None
        if self.inicio is None:
            self.fim = None

        return paciente_atendido

    def listar(self):
        if self.esta_vazio():
            print('A fila está vazia!')
            return

        print('\n--- FILA DE ATENDIMENTO ---')
        atual = self.inicio
        posicao = 1
        while atual:
            p = atual.paciente
            print(f"{posicao} - {p.nome} - {p.idade} anos - [{p.prioridade}]")
            atual = atual.proximo
            print('---------------------\n')
#Testes
if __name__ == '__main__':
    fila = FilaAtendimento()
    #Adicionado os pacientes
    print('Chegada dos pacientes: Ana (Normal), Bruno (Normal), Carlos (Prioridade)')
    fila.adicionar(Paciente('Ana', 32, 'Normal'))
    fila.adicionar(Paciente('Bruno', 70, 'Normal'))
    fila.adicionar(Paciente('Carlos', 45, 'Prioridade'))
    #Carlos pula para frente da fila
    fila.listar()
    print(f"Total de pacientes na fila: {fila.tamanho()}\n")

    # Atendendo o primeiro paciente (Deve ser o Carlos)
    paciente = fila.atender()
    if paciente:
        print(f"ATENDENDO: {paciente.nome}")

    # Chegando um novo paciente (prioritário)
    print('\nChegou Maria (Prioridade)')
    fila.adicionar(Paciente('Maria', 80, 'Prioridade'))
    fila.listar()
    #Esvaziando a fila
    print(f"ATENDENDO: {fila.atender().nome}")
    print(f"ATENDENDO: {fila.atender().nome}")
    print(f"ATENDENDO: {fila.atender().nome}")

    print(f"\nA fila está vazia? {fila.esta_vazio()}")