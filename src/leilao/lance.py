# -*- coding: utf-8 -*-

from .usuario import Usuario


class Lance:

    def __init__(self, usuario: Usuario, valor: float):
        self.__usuario = usuario
        self.__valor = valor

    @property
    def usuario(self) -> Usuario:
        return self.__usuario

    @property
    def valor(self) -> float:
        return self.__valor
