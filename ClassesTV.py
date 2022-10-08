class TV():
    def __init__(self, marca, tipo, polegadas):
        self.marca = marca
        self.tipo = tipo
        self.polegadas = polegadas


TV1 = TV("Philco", "LED", "42")

TV2 = TV("Samsung", "OLED", "55")

TV3 = TV("LG", "QLED", "32")

print(TV1.marca, TV1.tipo)

print(TV2.marca, TV2.polegadas)

print(TV3.polegadas, TV3.tipo)
