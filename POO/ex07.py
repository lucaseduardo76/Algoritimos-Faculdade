class Carro():
    def __init__(self, consumo):
        self.consumo = consumo
        self.combustivel = 0
    
    def exibirCombustivel(self):
        return self.combustivel
    
    def andar(self, distancia):
        litrosPerdido = distancia/self.consumo

        if(self.combustivel > litrosPerdido and distancia > 0):
            self.combustivel -= litrosPerdido
            return round(litrosPerdido, 2)
        else:
            return False
    
    def abastecer(self, litros):
        if litros > 0:
            self.combustivel += litros
        else:
            return False
    

def _main_():
    fiatUno = Carro(10) #Faz 10km/L
    km = 212
    fiatUno.abastecer(100)
    
    fiatUno.andar(km)
    print(f"O consumo foi de {fiatUno.andar(km)} litros")
    print(f"O fiat uno ainda tem {fiatUno.exibirCombustivel()} litros de gasosa")

_main_()