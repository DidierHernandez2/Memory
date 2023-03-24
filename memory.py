

from random import *
from turtle import *
from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
cuenta=0 #Se añadio una variable contador
largo="nada" #Se añadio una variable de tipo string
pares=0 #Se añadio una variable contador
numerosromanos=["N","I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX", "XXI", "XXII", "XXIII", "XXIV", "XXV", "XXVI", "XXVII", "XXVIII", "XXIX", "XXX", "XXXI"]
#Se añadio una lista de numeros romanos del 0 al 31
indice=0
def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']
    global cuenta #Se añade la variable global cuenta
    global pares #Se añade la variable global pares
    cuenta=cuenta+1 #Cada que se ingrese a la funcion tap se hará un conteo
    print(f'Cuenta de Taps: {cuenta}') #Imprimimos la cantidad de taps que se llevan por cada tap que se hace
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        pares+=1 #Cada que una tarjeta se quite se hará un conteo
        if (pares==32):#Si esta misma cuenta es igual a 32 (total de tarjetas que hay)
            print("Todos los cuadrados se han destapado") #Se imprimira un mensaje que diga que se han destapado todas las tarjetas
def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()
    global largo #Se añade la variable de tipo string
    global indice #Se añade la variable contador 
    global numerosromanos #Se añade la lista de numerosromanos
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        indice=tiles[mark] #A la variable de tipo contador se añade el numero que se imprimiria en la tarjeta
        largo=str(tiles[mark]) #Convertimos ese mismo numero en un string
        if len(largo)==3: #Si este string es más largo que 3 digitos se imprimira en una posición específica
            goto(x+8, y+15)
            color('black')
            write(numerosromanos[indice], font=('Arial', 10, 'normal'))#Se imprime el numero en romano
        elif len(largo)==4:
            goto(x+2, y+15)
            color('black')
            write(numerosromanos[indice], font=('Arial', 10, 'normal'))
        elif len(largo)>=5:
            goto(x, y+15)
            color('black')
            write(numerosromanos[indice], font=('Arial', 5, 'normal'))
        else:#Tenemos todas las opciones de largo que hay para los numeros romanos y su posicion especifica
            goto(x+20, y+15)
            color('black')
            write(numerosromanos[indice], font=('Arial', 10, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
