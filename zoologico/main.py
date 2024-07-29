from animal import Animal
from mamifero import Mamifero
from ave import Ave
from reptil import Reptil


def main():
    leao = Mamifero("Leão", 5, True)
    papagaio = Ave("Papagaio", 2, True)
    cobra = Reptil("Cobra", 4, "escamas")
    
    animais = [leao, papagaio, cobra]
    
    for animal in animais:
        print(f"Nome: {animal.nome}, Idade: {animal.idade}")
        animal.fazer_som()
        animal.movimentar()
        print()  

if __name__ == "__main__":
    main()