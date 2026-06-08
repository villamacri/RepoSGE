#want_greet= 'S'

#while want_greet == 'S':
#    print("Hola")
#    want_greet = input("¿Quieres saludar de nuevo? (S/N): ").upper()
#print ("Adiós")

want_greet ='S'
valid_options =0
while want_greet =='S':
    print("Hola qué tal!")
    want_greet = input("¿Quiere otro saludo?[S/N]")
    if want_greet not in 'SN':
        print("No le he entendido pero le saludo")
        want_greet ='S'
        continue
    valid_options +=1
print(f'{valid_options}respuestas válidas')
print('Que tenga un buen día')