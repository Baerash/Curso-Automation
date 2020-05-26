#Dada una concesionaria de autos, 5 clientes van a pedir un auto, debe preguntarsele:
#Nombre y apellido del comprador, Marc, Puertas y Color
#Deben imprimirse los datos de cada compra y el precio total.


def brand_price(brand):
    if brand == 'Ford':
        marca = 100000
    elif brand == 'Chevrolet':
        marca = 120000
    elif brand == 'Fiat':
        marca = 80000
    return marca

def doors_price(doors):
    if doors == '2':
        puertas = 50000
    elif doors == '4':
        puertas = 65000
    elif doors == '5':
        puertas = 78000
    return puertas

def colour_price(colour):
    if colour == 'Blanco':
        color = 10000
    elif colour == 'Azul':
        color = 20000
    elif colour == 'Negro':
        color = 30000
    return color

def precio_total(marca,puertas,color):
    return marca+puertas+color



i=0

while i < 5:
    print('Bienvenido a concensionarias Python, por favor complete el siguiente formulario para obtener su presupuesto:')
    nombre = (input('Nombre y Apellido: '))
    brand = (input('Marca (Ford, Chevrolet, Fiat): '))
    doors = (input('Número de puertas (2, 4, 5): '))
    colour = (input('Color (Blanco, Azul, Negro): '))
    marca = brand_price(brand)
    puertas = doors_price(doors)
    color = colour_price(colour)
    precio_total(marca,puertas,color)
    print('Estimado/a '+nombre+' si esta interesado en comprar el auto '+str(brand)+' con '+str(doors)+' puertas y de color '+str(colour)+' debería pagar $'+str(precio_total(marca,puertas,color))+'. Gracias por su consulta!')
    i=i+1

    