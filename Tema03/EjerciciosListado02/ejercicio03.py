listaInmuebles=[
    {'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
    {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
    {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
    {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
    {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}
    ]

def buscarInmueblesPorPresupuesto(listaInmuebles, presupuesto):
    precio=0.0
    listaFiltrada=[]
    for inmueble in listaInmuebles:
        if inmueble["zona"]=='A' and inmueble['garaje'] is True:
            precio=(inmueble['metros']*1000+inmueble['habitaciones']*5000 + 15000)*(1-(2026-inmueble['año'])/100)
    