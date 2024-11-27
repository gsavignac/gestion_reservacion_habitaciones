from collections import defaultdict

class Reservacion:
    def __init__(self, id, cliente, nro_habitacion, fecha_entrada, fecha_salida):
        self.id = id
        self.cliente = cliente
        self.nro_habitacion = nro_habitacion
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida

class GestionReservacion:
    def __init__(self):
        self.reservaciones = defaultdict(list)

    # agregando una nueva reserva de habitacion
    def agregar(self, reserva):
        self.reservaciones[reserva.nro_habitacion].append(reserva)
        print(f"- Reservacion para el cliente {reserva.cliente} en la habitación nro: {reserva.nro_habitacion} creada con éxito.")

    # cancelando una reservacion
    def cancelar(self, id):
        for reservaciones in self.reservaciones.items():
            for recerva in reservaciones:
                if recerva.id == id:
                    reservaciones.remove(recerva)
                    print(f"- Reservacion nro: {id} cancelada.")
                    return
                
        print(">> No se encontraron resultados")