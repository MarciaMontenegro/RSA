# RSA
 -INTEGRANTES:
 
			JOAQUIN MUÑOZ
			JOSUE CARPIO
			MARCIA MONTENEGRO
			
      
-FUNCIONAMIENTO DEL RSA_KEY_GENERATOR:
Para una mejor explicacion del algoritmo, lo dividiremos en partes:

1. Para hallar P:

	Utilizamos la funcion RANDOMGEN_PRIMOS(K), que genera un primo de forma aleatoria con MILLER RABIN de un tamaño determinado "K".
	
2. Para hallar Q:
	Utilizamos la misma funcion que utilizamos para P, pero tiene un while que comprueba que P no sea igual a Q.
	
3. Para hallar N:
	Multiplicamos P por Q.
	
4. Para hallar Φ(n):
	Como ambos numeros son primos, debemos separarlo como Φ(P) y Φ(Q).
	Φ(P) = P-1
	Φ(Q) = Q-1
	Finalmente solo multiplicamos ambos resultados
	Φ(N) = Φ(P) * Φ(Q)
	
5. Para hallar E:
	Se genera aleatoriamente el numero E, desde el 3 hasta el n-1 para que sea coprimo.
	Posterior a esto, utilizamos un bucle while que compruebe que el GCD de E y Φ(N) sea igual a 1.
	Esto lo hacemos con la funcion EUCLIDES.
	
6. Para hallar D:
	Se debe cumplir que ed sea congruente con 1 (mod Φ(N)), y esto lo hacemos hallando la inversa de e.
	
-
