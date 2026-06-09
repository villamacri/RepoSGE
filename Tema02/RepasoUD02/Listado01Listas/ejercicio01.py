listado = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6]

# for i in range(len(listado)):
#    if listado[i] < 0:
#        listado[i]=0
#
# print(listado)

for i, num in enumerate(listado):
    if num < 0:
        listado[i] = 0

print(listado)
