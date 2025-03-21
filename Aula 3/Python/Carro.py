# definindo o método construtor da classe
class Carro:
    def __init__(self, marca, modelo, ano, cor, placa):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.placa = placa
        self.is_running = False
        self.velocidade = 0
        self.marcha = 0 # Marcha ré será -1
    
    # Método de apresentação
    # Método de classe
    def __str__(self):
        return f"""
O carro de Marca {self.marca} e modelo {self.modelo}
do ano {self.ano} e cor {self.cor} saiu da loja e hoje tem a placa
{self.placa}
            """
    
    # método de instância
    @classmethod
    def cadastro_venda(cls):
        marca = input("Digite aqui a marca do carro comprado: ")
        modelo = input("Digite aqui o modelo do carro comprado: ")
        ano = int(input("Digite aqui o ano do carro comprado: "))
        cor = input("Digite aqui a cor do carro comprado: ")
        placa = input("Digite aqui a placa do carro comprado: ")
        return cls(marca, modelo, ano, cor, placa)
    
    
    def ligar_carro(self):
        if not self.is_running:
            self.is_running = True
            print("O carro foi ligado..... RUMRUMRUMRUM")
        else:
            print("O carro já esta ligado!!!")
    
    # montar um acelerador que ira acelerar com base na marchar definida
    def acelerar(self):
        if self.is_running and self.marcha == 0:
            self.marcha = 1
            self.velocidade += 30
        elif self.is_running and self.marcha == 1:
            self.marcha = 2
            self.velocidade += 25
        elif self.is_running and self.marcha == 2:
            self.marcha = 3
            self.velocidade += 15
        elif self.is_running and self.marcha == 3:
            self.marcha = 4
            self.velocidade += 10
        elif self.is_running and self.marcha == 4:
            self.marcha = 5
            self.velocidade += 5
        elif self.is_running and self.marcha == 5:
            self.marcha = 6
            self.velocidade += 5
            if self.velocidade > 160:
                self.velocidade = 160
        else:
            print(f"O carro {self.modelo} esta desligado precisa ligar o carro primeiro!!!")
        print(f"O carro esta na marcha {self.marcha} e velocidade do carro é {self.velocidade}km/h")

    def passar_marcha_re(self):
        if self.is_running and 0 >= self.marca <= 1:
            dicio = {-1: "Ré", 0:"Neutro"}
            self.marcha = -1
            self.velocidade += 3
            print(f"O carro esta na marcha {dicio[self.marcha]} e velocidade do carro é {self.velocidade}km/h")

    def freiar(self):
        if self.is_running and self.velocidade > 0:
            self.velocidade -= 5
            print(f"A velocidade do carro é {self.velocidade}km/h")
        else:
            print(f"O carro {self.modelo} esta desligado ou sua velocidade já é 0 km/h precisa ligar o carro primeiro!!!")



# para o carro da a ré ele precisa esta entre 1 km/h ou parado

# e o carro precisa ser desligado