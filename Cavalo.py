from AnimalCorrida import AnimalCorrida


class Cavalo(AnimalCorrida):
    def __init__(self, velocidade, nome, cor):
        super().__init__(velocidade, nome, cor)
        self.__posicao_atual = 0

    def mover(self):
        self.__posicao_atual = self.__posicao_atual + self.velocidade * 4

        if self.__posicao_atual >= 200:
            print(f"{self.nome} terminou a corrida!!")
            return self.__posicao_atual

        print(f"posição do cavalo {self.nome} atualizada para {self.__posicao_atual}")
        return False
