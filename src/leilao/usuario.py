# -*- coding: utf-8 -*-


class Usuario:

    def __init__(self, nome: str):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome
