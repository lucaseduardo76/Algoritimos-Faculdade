class Ingresso():
    def __init__(self, nome, valor):
        self.nomeEvento = nome
        self.valor = valor

    def exibirValor(self):
        return self.valor
    
    def __str__(self):
        return [
           self.nomeEvento,
           self.valor         
        ]
    


def _main_():
    vaquejada = Ingresso('Vaquejada', 968)
    gospel = Ingresso('Show de Thalles', 1134)

    ingresso = gospel

    print(f'O valor do ingresso para a {ingresso.__str__()[0]} é R$ {ingresso.__str__()[1]},00')

_main_()