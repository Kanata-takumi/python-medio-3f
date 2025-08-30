
def ejercicio1( a, b ):
	print( f"{a | b = }" )


def ejercicio2( a, b ):
	print( f"{a & b = }" )


def ejercicio3( a, b ):
	print( f"{a.symmetric_difference(b) = }" )


def ejercicio4( a, b ):
	print( f"a {'es' if a.issubset(b) else 'no es'} subconjunto de b" )


def ejercicio5( a ):
	print( f"a tiene {len(a)} elementos" )

if __name__ == "__main__":
	a = {1,2,3,4,5,6}
	b = {1,23,5,6}

	print()
	print(f"{a = }")
	print(f"{b = }")
	print()

	ejercicio1( a, b )
	print()

	ejercicio2( a, b )
	print()

	ejercicio3( a, b )
	print()

	ejercicio4( a, b )
	print()

	ejercicio5( a )
	print()
