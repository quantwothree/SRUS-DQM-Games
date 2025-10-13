from __future__ import annotations
from player import Player

class PlayerBNode:
    def __init__(self, player: Player) -> None:
        self._player: Player = player
        self._left_bnode = None
        self._right_bnode = None

    @property
    def player(self) -> Player:
        return self._player

    @property
    def left_bnode(self) -> PlayerBNode:
        return self._left_bnode

    @property
    def right_bnode(self) -> PlayerBNode:
        return self._right_bnode

    @player.setter
    def player(self, player: Player) -> None:
        self._player = player

    @left_bnode.setter
    def left_bnode(self, bnode: PlayerBNode) -> None:
        self._left_bnode = bnode

    @right_bnode.setter
    def right_bnode(self, bnode: PlayerBNode) -> None:
        self._right_bnode = bnode


