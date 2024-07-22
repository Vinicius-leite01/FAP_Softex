def bem_vindo():
    print("-----------------------------------")
    print("       PETSHOP DA FAMILIA   ")
    print("-----------------------------------")
    print("       SEJA BEM VINDO       ")
    print("-----------------------------------")

def menu():
    print("menu:")
    print("1 - banho e tosa")
    print("2 - cadastrar ")
    opcao = int(input("digite sua opção desejada: "))
    return opcao

def calcular_servicos(quant_horas, quant_servicos):
    pagar = quant_horas*quant_servicos*10
    return pagar

def main():
    bem_vindo()
    opcao = menu()

    if opcao == 1:
        quant_servicos = int(input("quantos serviços foram realizados: "))
        quant_horas = float(input("quantas horas meu funcionario trabalhou: "))
        cobrar = calcular_servicos(quant_horas, quant_servicos)
        print(f"o usuario solicitou {quant_servicos} serviços e meu funcionario precisou de {quant_horas} horas, logo o usuario precisara pagar o valor de {cobrar}")