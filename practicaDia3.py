"""DATOS DE ENTRADA  """
""" 1: Pedirle al usuario que ingrese un texto """
""" 2: Pedirle al usuario que ingrese 3 letras a su eleccion """
"""DATOS DE SALIDA  """
""" 1: Cuantas veces aparece cada letra .Se recomienda almacenar esas letras en una lista y luego usar
algun metodo propio de string que permita contar cuantas veces aparece un substring dentro del string
Tener en cuenta que las letras pueden ser ingresadas en mayusculas o minusculas (Convertir
a minusculas para la busqueda)"""

""" 2:  Mostrar cuantas palabras hay en total en todo el texto"""
""" 3:  Mostrar primera letra de texto y la ultima"""
""" 4: Mostrar el texto invertido"""
texto="Maria viaja siempre desde Cordoba"
listaLetras = {"letra1": "a", "letra2": "b", "letra3": "c"}
l1=listaLetras["letra1"].lower()
l2=listaLetras["letra2"].lower()
l3=listaLetras["letra3"].lower()
texto=texto.lower()
veces=texto.count(l1)
print(f"la letra l aparece {veces} veces")
veces=texto.count(l2)
print(f"la letra 2 aparece {veces} veces")
veces=texto.count(l3)
print(f"la letra 3 aparece {veces} veces")
palabras=texto.split()
print(f"El texto tiene {len(palabras)} palabras")
print(f"Primera letra {texto[0]} ")
print(f"Ultima letra {texto[-1]} ")
print(f"--Texto invertido --")
print(f"{texto[::-1]}")
