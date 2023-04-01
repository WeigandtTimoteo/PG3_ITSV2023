class Familia:
    def __init__(self, padre, madre, hijos):
        self.padre = padre
        self.madre = madre
        self.hijos = hijos

    def __str__(self):
        lista_hijos = ", ".join(self.hijos)
        return f"Padre: {self.padre}\nMadre: {self.madre}\nHijos: {lista_hijos}"

familia = Familia("Pepe", "María", ["Alejandro", "Laura"])
print(familia)
