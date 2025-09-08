from __future__ import annotations
from player import Player
from player_node import PlayerNode
from player_list import PlayerList
from player_list import KeyNotFoundException


class HashMap:
    def __init__(self, size : int) -> None:
        self.size = size
        self.hashmap = {}
        for i in range(size):
            self.hashmap[i] = PlayerList()

    def get_index(self, key: str | Player) -> int:
        if isinstance(key, Player):
            return hash(key) % self.size
        else:
            return Player.pearson_hash(key) % self.size

    def __setitem__(self, key: str | Player, name: str) -> None:
        if isinstance(key, str):
            uid = key
        else:
            uid = key.uid
        index = self.get_index(key)
        player_list = self.hashmap[index]

        if player_list.find(uid):
            player = player_list.find(uid)
            player.name = name #needs to add a @name setter in Player class
        else:
            player = Player(uid, name)
            node = PlayerNode(player)
            player_list.insert_head(node)

    def __getitem__(self, key: str | Player) -> Player:
        if isinstance(key, str):
            uid = key
        else:
            uid = key.uid
        index = self.get_index(key)
        player_list = self.hashmap[index]

        if player_list.find(uid):
            player = player_list.find(uid)
            return player
        else:
            raise KeyNotFoundException("Cannot find player")

    def __delitem__(self, key: str | Player) -> None:
        if isinstance(key, str):
            uid = key
        else:
            uid = key.uid
        index = self.get_index(key)
        player_list = self.hashmap[index]

        if player_list.find(uid):
            player_list.delete_at_key(uid)
        else:
            raise KeyNotFoundException("Cannot find player")

    def __len__(self) -> int:
        count = 0
        for i in range(self.size):
            player_list = self.hashmap[i]
            count += len(player_list)
        return count

    def display(self):
        for index in range(self.size): #needs to implement a __itr__ for PlayerList
            player_list = self.hashmap[index]
            if len(player_list) > 0:
                for player in player_list:
                    print(f"Index {index}: {player}")









