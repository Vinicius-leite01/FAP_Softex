numero = int(input('informe um número inteiro menor que 1000:'))

unidade = numero % 10

numero = (numero - unidade) // 10

dezena = numero % 10 

numero = (numero - dezena) // 10

centena = numero 

print(f"{centena} centena(s), {dezena} dezena(s) e {unidade} undade(s)")

