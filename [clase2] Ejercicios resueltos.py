def dividir( a, b ):
	"""Ejercicio 1"""
	try:
		res = a / b
	except ZeroDivisionError:
		print( "No se puede dividir por cero!" )
	else:
		print(res)


def sumar( a, b ):
	"""Ejercicio 2"""
	try:
		res = a + b
	except TypeError:
		print( "Debe ingresar dos números!" )
	else:
		print(res)


def buscarEnDiccionario( d, key ):
	"""Ejercicio 3"""
	try:
		valor = d[key]
	except KeyError as e:
		print(e)
		print( f"No existe la clave '{key}'" )
	else:
		print(valor)


def abrirOCrearArchivo( fileName ):
	"""Ejercicio 4"""
	try:
		file = open( fileName )

	except FileNotFoundError as e:
		print( "No se encontró el archivo!" )

		try:
			print( "Creando archivo..." )
			file = open( fileName, "w" )

		except Exception as e:
			print( "No se pudo crear el archivo." )
			print(e)
		else:
			print( "Archivo creado con éxito..." )
			file.close()

	else:
		print("Archivo abierto...")
		file.close()


def dividirV2( a, b ):
	"""Ejercicio 5"""
	try:
		a = float(a)
		res = a / b

	except ZeroDivisionError:
		print( "El segundo valor debe ser distinto de cero" )
		print( "No se puede dividir por cero!" )

	except ValueError:
		print( "El primer valor debe ser un número!" )

	else:
		print(res)


if __name__ == "__main__":

	print( "Ejercicio 1" )
	a = 3
	b = 0
	print( f"{a = }, {b = }" )
	dividir( a, b )
	print()

	print( "Ejercicio 2" )
	b = "asdljl"
	print( f"{a = }, {b = }" )
	sumar( a, b )
	print()

	print( "Ejercicio 3" )
	d = { "hola": 1 }
	key = "chau"
	print( f"{d = }, {key = }" )
	buscarEnDiccionario( d, key )
	print()

	print( "Ejercicio 4" )
	fileName = "archivoInexistente.txt"
	print( f"{fileName = }" )
	abrirOCrearArchivo( fileName )
	print()

	print( "Ejercicio 5" )
	print( 'Caso 1:' )
	a = 23
	b = 0
	print( f"{a = }, {b = }" )
	dividirV2( a, b )
	print()

	print( 'Caso 2:' )
	a = "dsjhg"
	b = 0
	print( f"{a = }, {b = }" )
	dividirV2( a, b )
	print()
