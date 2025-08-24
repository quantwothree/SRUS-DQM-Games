class PlayerList:
    def __init__(self):
        self._head = None
        self._tail = None

    def is_empty(self):
        if self._head is None:
            return True
        else:
            return False

    def insert_head(self, player_node):
        if self.is_empty():
            self._head = player_node
            self._tail = player_node
        else:
            player_node.next = self._head
            self._head.previous = player_node
            self._head = player_node

    def insert_tail(self, player_node):
        if self.is_empty():
            self._head = player_node
            self._tail = player_node
        else:
            self._tail.next = player_node
            player_node.previous = self._tail
            self._tail = player_node

    @property
    def head(self): #for accessing the private head
        return self._head

    @property
    def tail(self): #for accessing the private tail
        return self._tail


