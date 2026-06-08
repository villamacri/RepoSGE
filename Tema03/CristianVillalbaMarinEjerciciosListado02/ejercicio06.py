import random

def apostarMartingala(apuestaInicial, saldoInicial, probGanar, objetivo):
    saldo=saldoInicial
    apuestaActual=apuestaInicial

    while 0 < saldo < objetivo:
        if  apuestaActual > saldo:
            apuestaActual=saldo
        suerte = random.randint(1,100)

        if suerte <=(probGanar*100):
            saldo += apuestaActual
            apuestaActual = apuestaInicial
        else:
            saldo -= apuestaActual
            apuestaActual *= 2
    return saldo
