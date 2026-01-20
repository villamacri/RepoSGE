base="1234"
repeticiones=3

def generar_password(base, repeticiones):
    password=(base*repeticiones)+"!"
    return password

print(generar_password(base, repeticiones))