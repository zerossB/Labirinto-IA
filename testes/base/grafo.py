from base.functions import isPreto


class Linha(object):
    """
        Classe que representa um grafo direcionado

        1- Norte
        2- Sul
        3- Oeste
        4- Leste
        5- Nordeste
        6- Noroeste
        7- Suldeste
        8- Suldoeste
    """
    direcoes = [1, 2, 3, 4, 5, 6, 7, 8]

    def __init__(self,
                 x_ini=0, y_ini=0,
                 x_fim=0, y_fim=0,
                 peso=0, direcao=0):
        self.x_ini = x_ini
        self.y_ini = y_ini
        self.x_fim = x_fim
        self.y_fim = y_fim
        self.peso = peso
        self.direcao = direcao

    def distancia(self, base_pixels):
        if not self.direcao in self.direcoes:
            print("Direção não existente!")
            return

        count = 1
        x, y = self.x_ini, self.y_ini

        if self.direcao == 1:
            # Norte
            pass
        elif self.direcao == 2:
            # Sul
            while isPreto(base_pixels[x, y]):
                y = y + 1
                count = count + 1
                print(x, y)
        elif self.direcao == 3:
            # Oeste
            pass
        elif self.direcao == 4:
            # Leste
            pass

        self.x_fim = x
        self.y_fim = y
        self.peso = count

        print(self.peso)
