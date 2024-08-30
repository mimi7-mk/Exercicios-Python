class Quadrado:
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def mudar_valor_lado(self, novo_tamanho):
        self.tamanho_lado = novo_tamanho

    def retornar_valor_lado(self):
        return self.tamanho_lado

    def calcular_area(self):
        return self.tamanho_lado ** 2


quadrado = Quadrado(4)
print("Valor do lado:", quadrado.retornar_valor_lado())
print("Área:", quadrado.calcular_area())

quadrado.mudar_valor_lado(7)
print("Novo valor do lado:", quadrado.retornar_valor_lado())
print("Nova área:", quadrado.calcular_area())
