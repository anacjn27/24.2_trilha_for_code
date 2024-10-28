class Carro:
# o que está entre parenteses pertence a classe, o que está no corpo de def pertence a função init
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def chama_marca(self):
        print(self.marca)

    def chama_modelo(self):
        print(self.modelo)

ferrari = Carro("Ferrari", "250 GTO", "1962")

ferrari.chama_modelo()
