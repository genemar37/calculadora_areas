import math
import sys
import os
import time


opcion_cuadrado = "1"
opcion_circulo = "2"
opcion_triangulo = "3"
opcion_salida = "4"
contador_cuadrado = 0
contador_circulo = 0
contador_triangulo = 0


def calculo_cuadrado (valor_lado):
	area_cuadrado = round(valor_lado * valor_lado)
	return area_cuadrado

def calculo_circulo (valor_radio):
	area_circulo = math.pi * (valor_radio) ** 2
	area_circulo = round(area_circulo, 2)
	return area_circulo

def calculo_triangulo (valor_base, valor_altura):
	area_triangulo = round(valor_base * valor_altura) / 2
	return area_triangulo

def mostrar_totales(contador_cuadrado, contador_circulo, contador_triangulo):
    print(f"\nSe ha calculado el área del cuadrado: {contador_cuadrado} veces")
    print(f"\nSe ha calculado el área del círculo: {contador_circulo} veces")
    print(f"\nSe ha calculado el área del triángulo: {contador_triangulo} veces")


nombre_usuario = input("Hola, ¿cuál es tu nombre?: ")
print("\nBienvenido(a) a nuestra calculadora de áreas,", nombre_usuario, ":)")


while True:

	try:

		eleccion_usuario = input("\nSelecciona una de las siguientes figuras para calcular su área: \nPresiona 1 para cuadrado, 2 para círculo, 3 para triángulo o 4 para salir del sistema: ")


		if eleccion_usuario not in [opcion_cuadrado, opcion_circulo, opcion_triangulo, opcion_salida]:
			raise TypeError("Ups! Solo puedes ingresar las opciones mencionadas")


		if eleccion_usuario == opcion_cuadrado:
			valor_lado = float(input("\nHas seleccionado cuadrado. \nIngresa el valor de un lado del cuadrado: "))
			if valor_lado <= 0:
				raise NameError("Ups! Debes ingresar valores mayores a 0")
			print("El área del cuadrado es", calculo_cuadrado(valor_lado))
			contador_cuadrado +=1
			print(f"Se ha calculado el área del cuadrado {contador_cuadrado} veces")
			print("\n■")
			time.sleep(4)
			os.system("clear")


		elif eleccion_usuario == opcion_circulo:
			valor_radio = float(input("\nHas selecionado círculo. \nIngresa el valor del radio del círculo: "))
			if valor_radio <= 0:
				raise NameError("Ups! Debes ingresar valores mayores a 0")	
			print("El área del círculo es", calculo_circulo (valor_radio))
			contador_circulo +=1
			print(f"Se ha calculado el área del círculo {contador_circulo} veces")
			print("\n●")
			time.sleep(4)
			os.system("clear")


		elif eleccion_usuario == opcion_triangulo:
			valor_base = float(input("\nHas seleccionado triángulo. \nIngresa el valor de la base del triángulo: "))
			if valor_base <= 0:
				raise NameError("Ups! Debes ingresar valores mayores a 0")
			valor_altura = float(input("Ingresa el valor de la altura del triángulo: "))
			if valor_altura <= 0:
				raise NameError("Ups! Debes ingresar valores mayores a 0")
			print("El área del triángulo es", calculo_triangulo (valor_base, valor_altura))
			contador_triangulo +=1
			print(f"Se ha calculado el área del triangulo {contador_triangulo} veces")
			print("\n▲")
			time.sleep(4)
			os.system("clear")
			

		elif eleccion_usuario == opcion_salida:
			mostrar_totales(contador_cuadrado, contador_circulo, contador_triangulo)
			sys.exit("\nHas seleccionado la opción para salir del sistema. Muchas gracias por usar nuestro programa :)")


	except ValueError:
		print("Ups! Solo puedes escribir números")

	except TypeError as error:
		print(error)

	except NameError as error:
		print(error)