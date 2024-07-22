def solicitar():



def main():
    condicao = True

while condicao:
    numero = input('digite número inferior a 1000:')
    numero = int(numero)
    if numero > 0 and numero < 1000:
        condicao = False




centenas = numero // 100
resto_centena = numero % 100
dezenas = resto_centena // 10 
unidade = resto_centena % 10
if centenas > 0:   
    print(f"centenas {centenas}, dezenas {dezenas}, unidade {unidade}")
elif dezenas > 0:
    print(f" dezenas {dezenas}, unidade {unidade}")
else:
    print(f"unidade {unidade}")
main()