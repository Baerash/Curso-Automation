# 1-Ya no sabemos cuantos clientes tendremos,
# 2-Si el pedido no es uno de los autos en venta, entonces debe volver a preguntar hasta que si lo sea
# 3-Lo mismo con la cantidad de puertas y los colores.
# 4-Al final se pregunta si hay otro cliente o no, si hay otro cliente, entonces vuelve a preguntar todo.
# 5-Si la cantidad de clientes fue:
# --5.1: 0 a 5 personas no hay descuento
# --5.2: 6 a 10 personas: hay un descuento del 10%
# --5.3: 11 a 50 personas: hay un descuento del 15%
# --5.4: Más de 50 personas: El descuento es del 18%
# 6-Solo se va a mostrar que se vendió al final del programa

brand = {'Ford':100000,'Chevrolet':120000,'Fiat':80000}
doors = {2:50000,4:65000,5:78000}
colours = {'Blanco':10000,'Azul':20000,'Negro':30000}

def precio_parcial (marca,puertas,color):
    return brand[marca]+doors[puertas]+colours[color]

def desc_total (total_ventas):
    descuento = 0
    if 6 <= total_ventas <= 10:
        descuento = 0.9
    elif 11 <= total_ventas <= 50:
        descuento = 0.85
    elif total_ventas > 50:
        descuento = 0.82
    return descuento

seguir = 'Si'
ventas = []

while seguir == 'Si':
    marca = ''
    puertas = 0
    color = ''
    nombre = (input('Ingres Nombre y Apellido: '))
    while marca not in brand:
        marca = (input('Ingrese la marca: '))
    while puertas not in doors:
        puertas = int(input('Ingrese la cantidad de puertas: '))    
    while color not in colours:
        color = (input('Ingrese el color: '))  
    precio = precio_parcial(marca,puertas,color)   
    ventas.append({'nombre':nombre,'marca':marca,'puertas':puertas,'color':color,'precio':precio})
    seguir = (input('¿Desea cargar algún cliente adicional?: '))
descuento = desc_total (len(ventas))


for i in ventas:
    print('El cliente '+i['nombre']+' compró el auto '+i['marca']+' con '+str(i['puertas'])+' puertas y de color '+i['color']+' por un total de $'+str(i['precio']*descuento))



