from __future__ import annotations
from player_bnode import PlayerBNode

class PlayerBST:
    def __init__(self) -> None:
        self._root = None

    @property
    def root(self) -> PlayerBNode:
        return self._root

