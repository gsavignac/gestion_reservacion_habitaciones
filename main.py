import asyncio
from hotel_management.habitaciones import Habitacion, GestionHabitacion
from hotel_management.reservaciones import Reservacion, GestionReservacion
from hotel_management.clientes import Cliente, GestionCliente
from hotel_management.pagos import procesar_pago

async def main():

    # Instancia de los objetos principales
    gestion_habitacion = GestionHabitacion()
    gestion_reserva = GestionReservacion()
    gestion_cliente = GestionCliente()    

    # Agregando las habitaciones
    habitacion1 = Habitacion(1, "Individual", 110)
    habitacion2 = Habitacion(2, "Doble", 150)
    habitacion3 = Habitacion(3, "Matrimonial", 200)

    gestion_habitacion.agregar(habitacion1)
    gestion_habitacion.agregar(habitacion2)
    gestion_habitacion.agregar(habitacion3)

    print("\n")

    # Registrando los clientes
    cliente = Cliente(1, "Gustavo Savignac", "gustavo@gmail.com")
    cliente2 = Cliente(2, "Fiama Sandoval", "fiama@gmail.com")
    cliente3 = Cliente(3, "Alejandro Jimenez", "ale.jim@gmail.com")
    
    gestion_cliente.agregar(cliente)
    gestion_cliente.agregar(cliente2)
    gestion_cliente.agregar(cliente3)

    print("\n")

    # Verificar disponibilidad de habitaciones
    if gestion_habitacion.hab_disponible(habitacion1.nro_habitacion):

        reserva = Reservacion(1, cliente3.nombre, habitacion1.nro_habitacion, '2024-11-27', '2024-12-01')
        gestion_reserva.agregar(reserva)

        # Procesando pago de la habitacion
        await procesar_pago(110)

        # cambiando estatus de la habitacion
        habitacion1.cambiar_estatus(False)
        print("\n")


    if gestion_habitacion.hab_disponible(habitacion3.nro_habitacion):
        reserva = Reservacion(2, cliente.nombre, habitacion3.nro_habitacion, '2024-11-27', '2024-11-28')
        gestion_reserva.agregar(reserva)

        # Procesando pago de la habitacion
        await procesar_pago(200)

        # cambiando estatus de la habitacion
        habitacion3.cambiar_estatus(False)
        print("\n")

    if gestion_habitacion.hab_disponible(habitacion1.nro_habitacion):
        print(f"nro: {habitacion1.nro_habitacion}")
        reserva = Reservacion(2, cliente2.nombre, habitacion1.nro_habitacion, '2024-11-29', '2024-11-30')
        gestion_reserva.agregar(reserva)

        # Procesando pago de la habitacion
        await procesar_pago(200)

        # cambiando estatus de la habitacion
        habitacion3.cambiar_estatus(False)
        print("\n")

if __name__ == "__main__":
    asyncio.run(main())

