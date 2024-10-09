class Pessoa:
    def __init__(self, nome, peso, idade,comendo=False,andando=False,dormindo=False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo=comendo
        self.andando=andando
        self.dormindo=dormindo

    def andar(self):
        if self.andando == False:
            print("foi andar")
            self.andando=True

        else:
            print("Já parou de andar")

    def comer(self):
        if self.comendo == False:
            print("foi comer")
            self.comendo=True
        else:
            print("Já está comendo")

    def dormir(self):
        if self.dormindo == False:
            print("Está Dormindo")
            self.dormindo=True
        else:
            print("Já Acordou")

    def parardecomer(self):
        print("parar de comer")

    def parardeandar(self):
        print("parar de comer")

    def acordar(self):
        print("Acordou")


p1 = Pessoa("Wellington", 87, 51)
p1.nome = "Wellington Oliveira"
p1.andar()
p1.comer()
