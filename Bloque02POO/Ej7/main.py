from Serie import  Serie as Serie
from Videojuego import  Videojuego as Videojuego

listaSerie = []
listaVideo = []
s1 = Serie("El Señor de los anillos", False, "Ficción",8,  "Tolkin")
s2 = Serie("Juego de tronos", False, "Ficción",6,  "R.R. Martin")
v1 = Videojuego("GTA", 100, entregado = False, genero="Tiros", compania="Rockstar")

listaSerie.append(s1)
listaSerie.append(s2)
listaVideo.append(v1)

s1.entregar()
v1.entregar()

numeroEntregados = 0
for serie in listaSerie:
    if serie.is_entregado():
        numeroEntregados +=1
        print(serie.titulo)

print("El numero de series entregadas es: " + str(numeroEntregados))

numeroEntregadosJuegos = 0
for juego in listaVideo:
    if juego.is_entregado():
        numeroEntregadosJuegos += 1
        print(juego.titulo)

print("El numero de series entregadas es: " + str(numeroEntregadosJuegos))







