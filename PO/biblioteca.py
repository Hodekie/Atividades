class Pessoa:
    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo=False
        self.andando=False
        self.dormindo=False

    def comer(self):
        if self.comendo==False:
            if self.andando==False:
                if self.dormindo==False:
                    print(f"{self.nome} foi comer")
                    self.comendo=True
                else:
                    print(f"{self.nome} não pode comer pois está dormindo")
            else:
                print(f"{self.nome} não pode comer pois está andando")
        else:
            print(f"{self.nome} já estava comendo")

    def dormir(self):
        if self.dormindo==False:
            if self.andando==False:
                if self.comendo==False:
                    print(f"{self.nome} foi dormir")
                    self.dormindo=True
                else:
                    print(f"{self.nome} não pode dormir pois está comendo")
            else:
                print(f"{self.nome} não pode dormir pois está andando")
        else:
            print(f"{self.nome} já está dormindo")

    def andar(self):
        if self.andando==False:
            if self.comendo==False:
                if self.dormindo==False:
                    print(f"{self.nome} está andando")
                    self.andando=True
                else:
                    print(f"{self.nome} não pode andar pois está dormindo")
            else:
                print(f"{self.nome} não pode andar pois está comendo")
        else:
            print(f"{self.nome} já está andando")


class Animal:
    def __init__(self, nome, cor):
        self.nome=nome
        self.cor=cor
        self.comendo=False

    def comer(self):
        print(f"{self.nome} está comendo")

class Gato(Animal):
    def __init__(self, nome, cor):
       super().__init__(nome,cor)

    def miar(self):
        print(f"O {self.nome} foi miando...")
    def comer(self):
        print(f"O {self.nome} está brincando")

class Cachorro(Animal):
    def __init__(self, nome, cor):
       super().__init__(nome,cor)

    def latir(self):
        print(f"O {self.nome} está latindo...")
    def comer(self):
        print(f"O {self.nome} está mordendo o osso")

class Vaca(Animal):
    def __init__(self, nome, cor):
       super().__init__(nome,cor)

    def muge(self):
        print(f"O {self.nome}  muuuuu...")
    def comer(self):
        print(f"A {self.nome} está comendo mato")

class Coelho(Animal):
    def __init__(self, nome, cor):
       super().__init__(nome,cor)

    def gruhindo(self):
        print(f"O {self.nome} foi gruhiar...")
    def comer(self):
        print(f"O {self.nome} está pulando alto")

class Atleta:
    def __init__(self, nome, peso):
        self.nome=nome
        self.peso=peso
        self.aquecido=False
        self.aposentado=False

    def aposentar(self):
        if self.aposentado==False:
            print(f"{self.nome} foi aposentado com sucesso!")
            self.aposentado=True
        else:
            print(f"{self.nome} não pode aposentar pq já está na rede")


    def aquecer(self):
        if self.aquecido==False:
            print(f"{self.nome} foi aquecer com sucesso!")
            self.aquecido=True
        else:
            print(f"{self.nome} não pode aquecer pq já está aquecendo")

class Corredor(Atleta):
    def __init__(self, nome, peso):
       super().__init__(nome,peso)

    def correr(self):
        if self.aquecido==True:
            if self.aposentado==False:
                print(f" O {self.nome} foi correr")
            else:
                print(f" O {self.nome} não pode aquecer pq já está aposentado")
        else:
            print(f"{self.nome} não está aquecido")

class Nadador(Atleta):
    def __init__(self, nome, peso):
       super().__init__(nome,peso)

    def nadar(self):
        if self.aquecido==True:
            if self.aposentado==False:
                print(f" O {self.nome} foi nadar")
            else:
                print(f" O {self.nome} não pode nadar pq já está aposentado")
        else:
            print(f"{self.nome} não está aquecido")

class Ciclista(Atleta):
    def __init__(self, nome, peso):
       super().__init__(nome,peso)

    def pedalar(self):
        if self.aquecido==True:
            if self.aposentado==False:
                print(f" O {self.nome} foi pedalar")
            else:
                print(f" O {self.nome} não pode pedalar pq já está aposentado")
        else:
            print(f"{self.nome} não está aquecido")

class triatleta(Nadador, Ciclista, Corredor):
    def __init__(self, nome, peso):
       super().__init__(nome,peso)















