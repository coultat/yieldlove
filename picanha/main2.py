from dictionary import darcarta
# tocar todo lo que quieras


def repartoinicial(cartas):
    jugador = []
    maquina = []
    x = 0
    while x < 4:
        if x < 2:
            jugador.append(cartas[x])
            x = x + 1
        else:
            maquina.append(cartas[x])
            x = x + 1
    return jugador,maquina

def sumarcartas(mano):
    #totalcartas = len(mano)
    suma = 0
    count = 0
    ases = 0
    while count < len(mano):
        try:
            suma = suma + mano[count][0]
            if mano[count][0] == 1:
                ases += 1
                suma -= 1
        except TypeError:
            suma = suma + 10
        finally:
            count += 1
    while ases > 0:
        if suma + 11 > 21:
            suma += 1
            ases -= 1
        else:
            suma += 11
            ases -=1
    return suma

def darunacarta(pooldecartas, contador):

    carta = pooldecartas[contador-1]
    return carta




pooldecartas = pillarcartas()#cartas barajadas
cartasj, cartasm = repartoinicial(pooldecartas)#mano de cada uno de los jugadores y por donde va la baraja
contador = 4
totalcartas = 0
totalcartasm = 0
while True:
    print(f"Máquina que puedes ver {cartasm[0]}\nEstas son tus cartas: {cartasj}")
    totalcartas = sumarcartas(cartasj)
    if totalcartas > 21:
        print(f"\nHas perdido! La suma de tus cartas es {totalcartas}")
        break
    print(f"\nY esta es la suma de todas: {totalcartas}")
    turno = input(f"\n¿Sigues?\n")
    if(turno != 'n' and turno != 'N'):#no tocar esta mierda, parece que funciona bien
        contador += 1
        cartanueva = darunacarta(pooldecartas, contador)
        cartasj.append(cartanueva)
    else:
        break

while True and totalcartas < 21:
    totalcartasm = sumarcartas(cartasm)
    print(f"Estas son las cartas de la máquina {cartasm}")
    print(f"\nEste es el total de cartas de la máquina {totalcartasm}")
    if totalcartasm < totalcartas and totalcartasm < 21:
        contador += 1
        cartanueva = darunacarta(pooldecartas, contador)
        cartasm.append(cartanueva)
        totalcartasm = sumarcartas(cartasm)
    else:
        break
if (totalcartasm >= totalcartas and totalcartasm <= 21) or totalcartas > 21:
    print(f"\nLa máquina gana con estas cartas {cartasm}")
else:
    print(f"\nEl humano gana, estas son las cartas de la máquina {cartasm}")
