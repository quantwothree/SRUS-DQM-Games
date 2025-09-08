from __future__ import annotations
import random

class Player:
    def __init__(self, id : str, player_name : str) -> None:
        self._id = id
        self._player_name = player_name

    @property
    def uid(self):
        return self._id

    @property
    def name(self):
        return self._player_name

    @name.setter
    def name(self, new_name: str):
        self._player_name = new_name

    def __str__(self):
        return f"Player's ID: {self._id}, Name: {self._player_name}"

    @classmethod
    def pearson_hash(self, key: str) -> int:
        random.seed(42)
        pearson_table = list(range(256))
        random.shuffle(pearson_table)
        hash_ = 0
        for char in key:
            hash_ = pearson_table[hash_ ^ ord(char)]
        return hash_


    def __hash__(self):
        return self.pearson_hash(self.uid)

