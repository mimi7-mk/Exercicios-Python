class Bichinho:
    def __init__(self, nome, fome=0, tedio=0):
        self.nome = nome
        self.fome = fome
        self.tedio = tedio

    def alimentar(self, comida):
        self.fome = max(0, self.fome - comida)
    
    def brincar(self, tempo):
        self.tedio = max(0, self.tedio - tempo)
    
    def __str__(self):
        return f"Bichinho {self.nome} - Fome: {self.fome}, Tédio: {self.tedio}"

class Fazenda:
    def __init__(self, bichinhos):
        self.bichinhos = bichinhos

    def alimentar_brincar(self, comida, tempo):
        for bichinho in self.bichinhos:
            bichinho.alimentar(comida)
            bichinho.brincar(tempo)

    def __str__(self):
        return "\n".join(str(b) for b in self.bichinhos)

# Exemplo de uso
bichinhos = [Bichinho("Tama", fome=5, tedio=10), Bichinho("Gushi", fome=7, tedio=8)]
fazenda = Fazenda(bichinhos)

print(fazenda)  # Estado inicial
fazenda.alimentar_brincar(comida=4, tempo=5)
print(fazenda)  # Estado após alimentar e brincar
