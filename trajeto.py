class Transporte:
    def __init__(self, tipo, linha, destino):
        self.tipo = tipo
        self.linha = linha
        self.destino = destino

    def __str__(self):
        return f"{self.tipo} - Linha {self.linha} até {self.destino}"


class Onibus(Transporte):
    def __init__(self, linha, destino):
        super().__init__("Ônibus", linha, destino)


class BRT(Transporte):
    def __init__(self, linha, destino):
        super().__init__("BRT", linha, destino)


class Trajeto:
    def __init__(self):
        self.etapas = []

    def adicionar_etapa(self, transporte):
        self.etapas.append(transporte)

    def mostrar_trajeto(self):
        print("Caminho de casa para a faculdade:")
        for i, etapa in enumerate(self.etapas, start=1):
            print(f"Etapa {i}: {etapa}")


# Criando o trajeto de casa para a faculdade
trajeto = Trajeto()

trajeto.adicionar_etapa(Onibus("712", "Seropédica - Coelho Neto"))  # Primeiro ônibus
trajeto.adicionar_etapa(BRT("Expresso 61", "Estação Guadalupe"))     # Primeiro BRT
trajeto.adicionar_etapa(BRT("Parador 90", "Estação Fundão"))     # Segundo BRT
trajeto.adicionar_etapa(Onibus("01", "Gráfica"))         # Último ônibus

trajeto.mostrar_trajeto()
