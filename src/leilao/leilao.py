# -*- coding: utf-8 -*-
from src.leilao.lance import Lance


class Leilao:

    def __init__(self, descricao: str):
        self.__descricao = descricao
        self.__lances = []

    @property
    def descricao(self) -> str:
        return self.__descricao

    @property
    def lances(self) -> list:
        # devolve uma cópia rasa da lista
        return self.__lances[:]

    def propoe(self, lance: Lance) -> None:
        self.__lances.append(lance)
