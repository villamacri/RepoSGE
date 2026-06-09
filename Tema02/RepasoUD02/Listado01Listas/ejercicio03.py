notasAlumno = []
nota = 0.0
i = 0

while i < 5:
    i += 1
    nota = float(input("Diga la nota: "))
    if nota not in range(0, 11):
        print("Error, nota no válida")
        i -= 1
    else:
        notasAlumno.append(nota)

print(notasAlumno)
print(f"La media es: {sum(notasAlumno)/len(notasAlumno)}")
print(f"La nota mejor es {max(notasAlumno)} y la peor es {min(notasAlumno)}")
