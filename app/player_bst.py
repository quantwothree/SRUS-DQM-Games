from __future__ import annotations
from player_bnode import PlayerBNode
from player import Player

class PlayerBST:
    def __init__(self, root: PlayerBNode | None) -> None:
        self._root = root

    @property
    def root(self) -> PlayerBNode | None:
        return self._root

    def insert(self, player: Player) -> PlayerBNode:
        if self._root is None:
            self._root = PlayerBNode(player)
            return self._root
        else:
            current = self._root
            if player.name < current.player.name:
                current.left_bnode = PlayerBST(current.left_bnode).insert(player)
            elif player.name > current.player.name:
                current.right_bnode = PlayerBST(current.right_bnode).insert(player)
            else:
                self._root.player = player
            return self._root

    def search(self, name: str) -> Player | None:
        if self._root is None:
            return None
        elif self._root.player.name == name:
            return self._root.player
        else:
            if name < self._root.player.name:
                return PlayerBST(self._root.left_bnode).search(name)
            elif name > self._root.player.name:
                return PlayerBST(self._root.right_bnode).search(name)

