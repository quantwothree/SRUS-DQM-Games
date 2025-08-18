from __future__ import annotations

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

    def __str__(self):
        return f"Player's ID: {self._id}, Name: {self._player_name}]"


