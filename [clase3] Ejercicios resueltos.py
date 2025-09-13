MOSTRAR_EJEMPLOS = True

#Decorador general
def ejemplo( func ):
	def wrapper( *args, **kwargs ):
		if MOSTRAR_EJEMPLOS:
			print()
			print( func.__doc__ )
			func( *args, *kwargs )
			print()
		else:
			func( *args, **kwargs )
	return wrapper


@ejemplo
def mayor():
	"""Ejercicio 1"""
	try:
		a = int( input( "Ingrese un número: " ) )
		b = int( input("Ingrese otro número: " ) )
	except ValueError:
		print( "ERROR: Ingrese sólo números!" )
		#print( f"{a = }, {b = }")
	else:
		print( f"Dados {a = }, {b = }" )
		print( f"{a = }" if a > b else f"{b = }", "es mayor" )


def ingresarPalabras( *args ):
	"""Función auxiliar del ej2"""
	palabra = input( "Ingrese una palabra (vacío para terminar): " )
	if palabra:
		return ingresarPalabras( *args, palabra )
	else:
		return list( args )


@ejemplo
def buscarPalabra( palabra ):
	"""Ejercicio 2"""
	lista = ingresarPalabras()

	print(lista)
	print( f"'{palabra}'", "está" if palabra in lista else "no está", "en la lista" )


@ejemplo
def parOimpar( a ):
	"""Ejercicio 3"""
	print( f"{a} es", "impar" if a % 2 else "par" )


@ejemplo
def promedio( *args ):
	"""Ejercicio 4"""
	res = 0

	for arg in args:
		res += arg

	res = res / len(args) if len(args) else 0

	print(args)
	print(f"El promedio es {res}")


#Decorador del ej5
def argumentosInsuficientes( func ):
	def wrapper( *args, **kwargs ):
		"""Ejercicio 5"""
		try:
			func( *args, *kwargs )
		except TypeError:
			print( "Faltan argumentos!" )
	return wrapper


@ejemplo #toma los valores del decorador de abajo
@argumentosInsuficientes
def ej5( a ):
	pass


if __name__ == "__main__":

	#MOSTRAR_EJEMPLOS = False
	mayor()
	buscarPalabra("hola")
	parOimpar(5)
	promedio(3,4,5,6,7,5,7,8,1,10)
	ej5()

