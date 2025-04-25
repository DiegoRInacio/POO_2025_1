# QUESTÃO 1: Criação das classes CadastroPessoa, CadastroSala e AgendamentoSala

class CadastroPessoa:
    def __init__(self, nome, instituicao, cpf):
        self.nome = nome
        self.instituicao = instituicao
        self._cpf = cpf  # CPF encapsulado

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, novo_cpf):
        self._cpf = novo_cpf

    # QUESTÃO 2: Métodos resumo() e __str__()
    def resumo(self):
        return f"{self.nome} - {self.instituicao}"

    def __str__(self):
        return f"Nome: {self.nome}, Instituição: {self.instituicao}, CPF: {self.cpf}"

class CadastroSala:
    def __init__(self, nome_sala, local, capacidade):
        self.nome_sala = nome_sala
        self.local = local
        self.capacidade = capacidade

    # QUESTÃO 2: Métodos resumo() e __str__()
    def resumo(self):
        return f"{self.nome_sala} - {self.local}"

    def __str__(self):
        return f"Sala: {self.nome_sala}, Local: {self.local}, Capacidade: {self.capacidade}"

class AgendamentoSala:
    def __init__(self):
        self.agendamentos = []  # QUESTÃO 1: Inicializa lista de agendamentos

    # QUESTÃO 2: Método para adicionar agendamento
    def adicionar_agendamento(self, pessoa, sala):
        self.agendamentos.append((pessoa, sala))

    # QUESTÃO 2: Método para listar agendamentos
    def listar_agendamentos(self):
        return [f"{pessoa.nome} agendou {sala.nome_sala}" for pessoa, sala in self.agendamentos]

    # QUESTÃO 3: Buscar agendamentos de uma sala específica
    def buscar_por_sala(self, nome_sala):
        return [pessoa.nome for pessoa, sala in self.agendamentos if sala.nome_sala == nome_sala]

    # QUESTÃO 3: Buscar salas agendadas por uma pessoa
    def buscar_por_pessoa(self, nome_pessoa):
        return [sala.nome_sala for pessoa, sala in self.agendamentos if pessoa.nome == nome_pessoa]

    # QUESTÃO 3: Método extra - carregar dados de listas
    def carregar_de_listas(self, lista_de_pessoas, lista_de_salas):
        for pessoa, sala in zip(lista_de_pessoas, lista_de_salas):
            self.adicionar_agendamento(pessoa, sala)


# Criando pessoas
pessoa1 = CadastroPessoa(nome="Ana Souza", instituicao="Universidade A", cpf="123.456.789-00")
pessoa2 = CadastroPessoa(nome="Carlos Silva", instituicao="Instituto B", cpf="987.654.321-00")

# Criando salas
sala1 = CadastroSala(nome_sala="Sala 101", local="Bloco A", capacidade=30)
sala2 = CadastroSala(nome_sala="Sala 202", local="Bloco B", capacidade=50)

# Criando agendador
agendamento = AgendamentoSala()

# Adicionando agendamentos
agendamento.adicionar_agendamento(pessoa1, sala1)
agendamento.adicionar_agendamento(pessoa2, sala2)
agendamento.adicionar_agendamento(pessoa1, sala2)  # Ana também agenda a sala 202

# Listando todos os agendamentos
print("\nTodos os Agendamentos:")
for info in agendamento.listar_agendamentos():
    print(info)

# Buscando por uma sala específica
print("\nQuem agendou a Sala 202?")
for nome in agendamento.buscar_por_sala("Sala 202"):
    print(nome)

# Buscando todas as salas agendadas por uma pessoa
print("\nSalas agendadas por Ana Souza:")
for nome_sala in agendamento.buscar_por_pessoa("Ana Souza"):
    print(nome_sala)
