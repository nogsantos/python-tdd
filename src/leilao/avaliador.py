# -*- coding: utf-8 -*-
import sys
from .leilao import Leilao


class Avaliador:

    def __init__(self):
        self.__maior_lance = sys.float_info.min
        self.__menor_lance = sys.float_info.max

    def avalia(self, leilao: Leilao):
        for lance in leilao.lances:
            if lance.valor > self.__maior_lance:
                self.__maior_lance = lance.valor
            if lance.valor < self.__menor_lance:
                self.__menor_lance = lance.valor

    @property
    def maior_lance(self):
        return self.__maior_lance

    @property
    def menor_lance(self):
        return self.__menor_lance
