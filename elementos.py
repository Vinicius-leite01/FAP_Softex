#numeros = [10, 20, 30, 40]
#numeros.insert(1,15)
#print(numeros)

#numeros = [10, 20, 30]
#removido = numeros.pop(1)
#print(removido)
#print(numeros)

frutas = ['maçã', 'goiaba', 'melancia', 'pêra', 'jaca']
print(frutas)
print(frutas[2])
frutas[1] = 'banana'
print(frutas)
frutas.append('abacate')
print(frutas)
del frutas[2]
print(frutas)
removido = frutas.pop(-1)
print(removido)
print(frutas)
print("tamanho da lista: ", len(frutas))
for fruta in frutas:
    if fruta.upper() != 'BANANA':
        print(fruta)