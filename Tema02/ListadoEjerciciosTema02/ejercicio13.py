abecedario=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numMul=3

for j in range(len(abecedario)-1, -1, -1):
    if j % numMul == 0:
        abecedario.pop(j)

print(abecedario)