import asyncio
import random

async def procesar_pago(monto):
    print(f"- Procesando pago, espere por favor...")

    # generar un tiempo de espera
    await asyncio.sleep(random.randint(1, 3))

    print(f"- El pago por ${monto} fue realizado con éxito.")
    return True

