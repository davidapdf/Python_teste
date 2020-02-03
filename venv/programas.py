class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

        def __str__(self):
            return f'Nome: {self.nome} Likes: {self.likes}'
    @property
    def likes(self):
        return self._likes
    def dar_likes(self):
        self._likes +=1
    @property
    def nome(self):
        return self._nome

class Filme(Programa):
    def __init__(self,nome, ano, duracao):
        super().__init__(nome,ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} - {self.duracao} min - Likes: {self.likes}'

class Serie(Programa):
    def __init__(self,nome, ano, temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} - {self.temporadas} temporadas - Likes: {self.likes}'


vingadores = Filme("Vingadores",2019,160)
atlanta = Serie("atlanta",2015,10)
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()

atlanta.dar_likes()
atlanta.dar_likes()

listinha = {vingadores,atlanta}

for programa in listinha:
    print(programa)
