class PlayerList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        if self._head is None:
            return True
        else:
            return False

    def insert_head(self, player_node):
        if self.is_empty():
            self._head = player_node
        else:
            player_node.next = self._head
            self._head.previous = player_node
            self._head = player_node

    @property
    def head(self): #for accessing the private head in unit tests
        return self._head