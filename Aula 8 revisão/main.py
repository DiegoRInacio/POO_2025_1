class Loja:
    def __init__(self):
        self.catalogo = []

    def realizar_venda(self):
        pass

    def oferecer_promocao(self):
        pass

    def adicionar_produto(self, produto, valor):
        item = {produto: valor}
        self.catalogo.append(item)
        print(f"Produto '{produto}' adicionado ao catálogo com o valor de R${valor:.2f}.")

    def remover_produto(self, produto):
        for item in self.catalogo:
            if produto in item:
                self.catalogo.remove(item)
                print(f"Produto '{produto}' removido do catálogo.")
                return
        print(f"Produto '{produto}' não encontrado no catálogo.")

    def listar_produtos(self):
        if not self.catalogo:
            print("O catálogo está vazio.")
        else:
            print("Produtos disponíveis no catálogo:")
            for produto in self.catalogo:
                for chave, valor in produto.items():
                    print(f"{chave.capitalize()} : R${valor:.2f}")
                print("-" * 30)


class Conta:
    def __init__(self, nome_cliente, numero_conta, agencia, saldo=0.0):
        self.nome_cliente = nome_cliente
        self.numero_conta = numero_conta
        self.agencia = agencia
        self.saldo = saldo
        self.limite_cheque_especial = 500.0
        self.limite_cartao = 1000.0
        self.__pix = None
        self.__senha = None

    def cadastrar(self):
        if self.__senha is None:
            self.__senha = input("Defina sua senha: ")
            print(f"Conta cadastrada com sucesso para {self.nome_cliente}!")
        else:
            print("A conta já foi cadastrada com senha.")

    def autenticar(self, senha):
        return self.__senha == senha

    def cadastrar_pix(self, chave_pix):
        if self.__pix is None:
            self.__pix = chave_pix
            print("Chave Pix cadastrada com sucesso.")
        else:
            print("Chave Pix já cadastrada.")

    def pix(self, chave_pix_origem, valor, conta_destino):
        if self.__pix != chave_pix_origem:
            print("Chave Pix incorreta.")
            return
        if self.saldo >= valor:
            self.saldo -= valor
            conta_destino.saldo += valor
            print(f"Pix de R${valor:.2f} enviado para {conta_destino.nome_cliente}.")
        else:
            print("Saldo insuficiente para realizar o Pix.")

    def cheque_especial(self, valor):
        if valor <= self.limite_cheque_especial:
            self.saldo -= valor
            print(f"Cheque especial de R${valor:.2f} utilizado.")
        else:
            print("Limite do cheque especial excedido.")

    def cartao_credito(self, valor):
        if valor <= self.limite_cartao:
            print(f"Pagamento de R${valor:.2f} no cartão de crédito realizado.")
        else:
            print("Limite do cartão excedido.")

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")

    def debito(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Pagamento de R${valor:.2f} no débito realizado.")
        else:
            print("Saldo insuficiente para débito.")


class LojaFisica(Loja):
    def __init__(self):
        super().__init__()
        self.__desconto = None

    def realizar_venda(self, metodo, conta, item_index, produto):
        try:
            valor = self.catalogo[item_index][produto]
        except (IndexError, KeyError):
            print("Produto ou índice inválido.")
            return

        if self.__desconto is not None:
            valor = valor - (valor * self.__desconto / 100)

        self.efetuar_pagamento(metodo, conta, valor)
        print(f"Venda do produto '{produto}' realizada com sucesso no valor de R${valor:.2f}.")
        del self.catalogo[item_index]

    def oferecer_promocao(self, desconto):
        self.__desconto = desconto
        print(f"Desconto de {desconto}% definido!")

    def efetuar_pagamento(self, metodo: str, conta: Conta, valor: float):
        print(f"\nIniciando pagamento no valor de R${valor:.2f} via '{metodo}'...")
        if metodo == 'pix':
            conta.pix(conta._Conta__pix, valor, conta)  # cuidado: chave pix precisa estar cadastrada
        elif metodo == 'cheque_especial':
            conta.cheque_especial(valor)
        elif metodo == 'cartao_credito':
            conta.cartao_credito(valor)
        elif metodo == 'debito':
            conta.debito(valor)
        else:
            print("Método de pagamento inválido.")

conta1 = Conta("Zé da Manga", "12345-6", "0001", saldo=500.0)
conta1.cadastrar()
conta1.cadastrar_pix("diego@pix.com")

loja = LojaFisica()
loja.adicionar_produto("Camiseta", 100.0)
loja.adicionar_produto("Tênis", 200.0)
loja.listar_produtos()

loja.oferecer_promocao(10)
loja.realizar_venda("pix", conta1, 0, "Camiseta")

print(f"\nSaldo final: R${conta1.saldo:.2f}")