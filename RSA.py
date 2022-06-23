import random
s = 40
def EUCLIDES(a, b):
    if b == 0 :
        return a
    else:
      return EUCLIDES(b, a % b)
def EUCLIDES_EXT(a, b):
    if a == 0 :
        return b,0,1
    mcd,x1,y1 = EUCLIDES_EXT(b%a, a)
    x = y1 - (b//a) * x1
    y = x1
    return mcd,x,y
def modulo(a,b):
    r=a%b
    if r < 0:
        r=r+ b;
    return r
def INVERSA(a,b):
    m,a,y=EUCLIDES_EXT(a,b)
    if a<0:
      a=modulo(a,b)
    return a
def EXPMOD(a,x,n):
  c=a%n
  r=1
  while(x>0):
    if x%2!=0:
      r=(r*c)%n
    c=(c*c)%n
    x=x//2
  return r
def ES_COMPUESTO(a, n, t, u):
  xi = EXPMOD(a,u,n)
  if xi == 1 or xi == n-1:
    return False
  for i in range(t):
    xi = EXPMOD(xi,2,n)
    if xi == n-1:
      return False
  return True
def MILLER_RABIN(n,s):
  t=0
  u=n-1
  while (u%2==0):
    u=u/2
    t=t+1
  for j in range(1,s):
    a=random.randint(2,n-1)
    if ES_COMPUESTO(a,n,t,u):
      return False
  return True
def RANDOMBITS(b):
    n=random.randint(0,(2**b)-1)
    m=(2**(b-1))+1
    n=n | m
    return n
def RANDOMGEN_PRIMOS(b):
    n=RANDOMBITS(b)
    while MILLER_RABIN(n,s) is False:
        n=n+2
    return n
#-------------------------RSA----------------------------
def RSA_KEY_GENERATOR(K):
  seguir = True
  while seguir:
    P = RANDOMGEN_PRIMOS(K)
    Q = RANDOMGEN_PRIMOS(K)
    if P != Q:
      seguir = False
  N = P*Q
  fi_P=P-1
  fi_Q=Q-1
  FI= fi_P * fi_Q
  seguir = True
  while seguir:
    E=random.randint(3,N-1)
    if (EUCLIDES(E, FI) == 1):
      seguir=False
  D = INVERSA(E,FI)
  #RESPUESTAS
  print("N es : ", N)
  print("E es : ", E)
  print("D es : ", D)
  return(N,E,D)
def CIFRADO(M,E,N):
  CIFRADO =EXPMOD(M,E,N)
  print("Cifrado = ", CIFRADO)
  return CIFRADO
def DESCIFRADO(C,D,N):
  DESCIFRADO = EXPMOD(C,D,N)
  print("Descifrado = ", DESCIFRADO)
  return DESCIFRADO
def ITEM1():
  BITS= int(input("Ingrese el tamaño de bits a generar el RSA:"))
  BITS//2
  MENSAJE=int(input("INGRESA LO QUE SE CIFRARA: "))
  N,E,D = RSA_KEY_GENERATOR(BITS)
 # CIFRADO(MENSAJE,E,N)
  DESCIFRADO(CIFRADO(MENSAJE,E,N),D,N)
#-----------------------------------
def ITEM2():
  N,E,D = RSA_KEY_GENERATOR(64)
  print("-----TABLA-----")
  for i in range(1,11):
    print(i)
    M=random.randint(2,N-1)
    print("M es:", M)
    DESCIFRADO(CIFRADO(M,E,N),D,N)
#---------------------------------------------
print("¿QUE DESEAS EJECUTAR?")
print("1 --> Item1: Cifrar y descifrar un mensaje ingresdo con RSA_KEY_GENERATOR")
print("2 --> Item2: Sistema RSA64 mostrando 10 valores de m aleatorios, cifrado y decifrado con los mismos N,E,D")
ELECCION=int(input("Ingresa tu eleccion: "))
if ELECCION == 1:
  ITEM1()
elif ELECCION == 2:
  ITEM2()
