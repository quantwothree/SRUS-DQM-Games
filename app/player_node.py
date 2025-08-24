class PlayerNode:
    def __init__(self, player):
        self._player = player
        self._next = None
        self._previous = None

    @property
    def player(self):
        return self._player

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, player_node):
        self._next = player_node

    @property
    def previous(self):
        return self._previous

    @previous.setter
    def previous(self, player_node):
        self._previous = player_node

    @property
    def key(self):
        return self._player.uid

    def __str__(self):
        return f"Player Node: {str(self._player)}"
