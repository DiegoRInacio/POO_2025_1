# Gasta mais memoria
#import Carro as Car

# Gasta menos memoria
from Carro import Carro as Car

carro1 = Car("Fiat", "Uno com escada em cima", 2009, "Branco", "XTS85GH")

carro2 = Car("VW", "Gol", 2007, "Vermelho", "GH12HF")

# USando o cadastro de vendas
#carro3 = Car.cadastro_venda()

print(carro1, "\n", carro2)

carro2.ligar_carro()

for i in range(30):
    carro2.acelerar()

for i in range(6):
    carro2.freiar()



