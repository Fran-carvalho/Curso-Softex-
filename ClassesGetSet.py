class salario:
    def __init__(self, salario=0):
        self._salario = salario

    def get_salario(self):
        return self._salario

    def set_salario(self, x):
        self._salario = x


var = salario()
var.set_salario(1212.00)
print(var.get_salario())

print(var._salario)
