class Cliente:
    def __init__(self, id, nombre, email):
        self.id = id
        self.nombre = nombre
        self.email = email

class GestionCliente:
    def __init__(self):
        self.clientes = {}

    # registrando nuevo cliente
    def agregar(self, cliente):
        self.clientes[cliente.id] = cliente
        print(f"- El cliente {cliente.nombre} fue agregado con éxito.")

    # retorna la informacion del cliente
    def buscar(self, id):
        return self.clientes.get(id, ">> No se encontraron resultados")

