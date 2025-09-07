dineroDisponible = 4000000

monedas = {
	"dolar": {
		"compra": 1200,
		"venta": 1100,
		"posee": 0
	},

	"euro": {
                "compra": 1200,
                "venta": 1100,
		"posee": 0
        },

	"libra": {
                "compra": 1200,
                "venta": 1100,
		"posee": 0
        },

	"yen": {
                "compra": 1200,
                "venta": 1100,
		"posee": 0
        },

	"real": {
                "compra": 1200,
                "venta": 1100,
		"posee": 0
        }
}


def comprar( moneda, cantidad ):
	precio = monedas[moneda]["compra"] * cantidad
	operacionExitosa = False

	if dineroDisponible - precio >= 0:
		dineroDisponible -= precio
		monedas[moneda]["posee"] = cantidad
		operacionExitosa = True

	return operacionExitosa


def vender( moneda, cantidad ):
	disponible = monedas[moneda]["posee"]
	operacionExitosa = False

	if  disponible - cantidad >= 0:
		dineroDisponible += cantidad * monedas[moneda]["venta"]
		operacionExitosa = True

	return operacionExitosa


def mostrarOpciones():
	print( """
********************************

1] Comprar Moneda Extranjera
2] Vender Moneda Extranjera

********************************
Ingrese un opción para continuar (o ninguna para Salir): """ )

	op = input()
	seleccion = "salir"
	match op:
		case "1":
			seleccion = "comprar"
		case "2":
			seleccion = "vender"

	return seleccion


def mostrarBalance():
	print(f"""
Pesos(ARS): ${dineroDisponible}

Nombre		|	Compra	|	Venta	|	Posee		|""" )
	#-------------------------------------------------------------------------
	#Dolar		|	$1200	|	$1100	|	0

	for moneda,detalles in monedas.items():
		print(f"""-------------------------------------------------------------------------
  {moneda.capitalize()}		|       ${detalles['compra']}   |       ${detalles['venta']}   |       {detalles['posee']}""")


def app():

	while True:
		mostrarBalance()

		seleccion = mostrarOpciones()

		match seleccion:
			case "comprar":
				menuCompra()
			case "vender":
				menuVenta()
			case "salir":
				break


if __name__ == "__main__":

	#app()
	mostrarBalance()
	print(mostrarOpciones())
