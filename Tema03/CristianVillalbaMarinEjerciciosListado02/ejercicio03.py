listaInmuebles=[
    {'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
    {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
    {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
    {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
    {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}
    ]

def calcularPrecio(inmueble):
    antiguedad=2026-inmueble['año']

    precio=(inmueble['metros']*1000+inmueble['habitaciones']*5000)

    if inmueble['garaje']:
        precio += 15000
    
    precio *= (1-antiguedad/100)
    if inmueble['zona']=='B':
        precio*=1.5

    return precio

def buscarInmueblesPorPresupuesto(listaInmuebles, presupuesto):
    listaFiltrada=[]

    for inmueble in listaInmuebles:
        precio_final=calcularPrecio(inmueble)

        if precio_final <= presupuesto:
            inmueble['precio']=precio_final
            listaFiltrada.append(inmueble)
    return listaFiltrada

def pintarListaFiltrada(listaFiltrada):
    for inmueble in listaFiltrada:
        print(f"{inmueble}")

presupuesto=100000
listaFiltrada=buscarInmueblesPorPresupuesto(listaInmuebles, presupuesto)
print("Estos son los inmuebles según su presupuesto: ")
pintarListaFiltrada(listaFiltrada)