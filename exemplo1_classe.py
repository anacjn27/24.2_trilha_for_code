class Carro:
    def __init__(self, modelo, cor, ano, preco):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.preco = preco
        self.ligado = False
        self.velocidade = 0
# ação
    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def acelerar(self):
        self.velocidade += 10

# carro1 é um objeto
carro1 = Carro('Fusca', 'Azul', 1998, 5000)
print(carro1.ligado, carro1.velocidade)
carro1.ligar()
carro1.acelerar()
print(carro1.ligado, carro1.velocidade)

