def genera_primos() -> list:
    DOSMIL=2000
    lista_primos=[]
    for i in range(2,DOSMIL):
        primo = True
        for j in range(2, i):
            if i % j == 0:
                primo = False
                break
        if primo:
            lista_primos.append(i)
    return lista_primos


numero = int(input("Introduce un numero: "))
numeros_primos = genera_primos()
for i in range(2000):
    if numero < numeros_primos[i]:
        print(numeros_primos[i])
        break



