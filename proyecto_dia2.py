"""pedir al uysuario nombre y ventas totales ,mostrar el 13 % de comision
para saber cuanto gano extra"""

nombre=input("Ingresa tu nombre")
ventas=input("Ingresa tus ventas totales")
comision=float(ventas)**0.13
ventasTotales=round(float(ventas)+comision,2)

print(f"${ventasTotales} usd")