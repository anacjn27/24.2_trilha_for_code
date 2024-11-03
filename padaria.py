class Padeiro:
    def __init__(self, nome):
        self.nome = nome
        self.dinheiro = 0
        self.paes = 0
        pass

    def assar_paes(self, quantidade):
        if quantidade > 6:
            print("A capacidade maxima do forno é 6.")
        else:
            self.paes += quantidade
            pass

class Cliente:
    def __init__(self, nome, dinheiro):
        self.nome = nome
        self.dinheiro = dinheiro
        self.paes = 0
        pass

    def comprar_paes(self, quantidade, padeiro):
        if quantidade > padeiro.paes:
            print("Não há pães suficientes para compra")
        elif self.dinheiro < quantidade * 0.75:
            print("Você não tem dinheiro o suficiente para comprar o pão")
        else:
# dinheiro é igual ao dinheiro do cliente menos a quantidade de pães comprada vezes o valor do pão
            self.dinheiro -= quantidade * 0.75
            self.paes += quantidade
            padeiro.dinheiro += quantidade * 0.75
            padeiro.paes -= quantidade * 0.75
            print('Compra realizada!')
            pass


padeiro1 = Padeiro('Joaquim')
cliente1 = Cliente('Maria', 2)
padeiro1.assar_paes(6)
cliente1.comprar_paes(5, padeiro1)