class Habitacion:
    
    def __init__(self, nro_habitacion, tipo, precio):
        self.nro_habitacion = nro_habitacion
        self.tipo = tipo
        self.precio = precio
        self.disponible = True

    def cambiar_estatus(self, nuevo_estatus):
        self.disponible = nuevo_estatus
        estatus = 'No Disponible'
        if(nuevo_estatus == True):
            estatus = 'Disponible'
        print(f"La habitacion nro: {self.nro_habitacion} se encuentra {estatus}\n")

class GestionHabitacion:
    def __init__(self):
        self.habitaciones = {}

    # registrar habitaciones al listado
    def agregar(self, habitacion):

        self.habitaciones[habitacion.nro_habitacion] = habitacion
        print(f"- La habitación nro: {habitacion.nro_habitacion} fue agregada con éxito.")

    # verificar si esta disponible la habitacion
    def hab_disponible(self, nro_habitacion):

        habitacion = self.habitaciones.get(nro_habitacion)

        if habitacion and habitacion.disponible:
            print(f"- La habitación nro: {nro_habitacion} está disponible.")
            return True
        
        print(f">> La habitación nro: {nro_habitacion} no se encuentra disponible.")
        return False

