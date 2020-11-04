# coding: utf-8
# license: GPLv3
from gameunit import Attacker

class Hero(Attacker):
    def __init__(self):
        self._HP = 100
        self._At = 50
        self._Exp = 0
        self._Name = name
    def attack(self, target):
        target._HP -= self.attack()