from player import Player
from player_node import PlayerNode

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

    def delete_at_head(self):
        if self.is_empty():
            raise IndexError("Can not delete from an empty list")
        elif self._head == self._tail: #for when list only has 1 node
            self._head = None
            self._tail = None
        else:
            self._head = self._head.next #Or can use self.head = self.head.next but needs to define a @head.setter
            self._head.previous = None #Or can use self.head.previous = None if already define a @head.setter

    #Use setters for head and tail in this case:
    def delete_at_tail(self):
        if self.is_empty():
            raise IndexError("Can not delete from an empty list")
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None

    def delete_at_key(self, key_to_delete):
        if self.is_empty():
            raise IndexError("Can not delete from an empty list")
        elif self.head == self.tail: #list has 1 node
            if self.head.key != key_to_delete: #if key is invalid (not in list)
                raise KeyError("Can not find key in list")
            else: # the 1 node in list is the node to be deleted
                self.delete_at_head()
                return
        else: # if list has more than 1 node, loop through to find the node to delete
            if self.head.key == key_to_delete:
                self.delete_at_head()
                return
            if self.tail.key == key_to_delete:
                self.delete_at_tail()
                return
            else:
                current_node = self.head.next
                while current_node:
                    if current_node.key == key_to_delete:
                        current_node.previous.next = current_node.next
                        current_node.next.previous = current_node.previous
                        return
                    else:
                        current_node = current_node.next
                raise KeyError("Can not find key in list")

    def display(self, forward = True):
        if forward:
            while self.head:
                print(self.head.player) # calls __str__ defined in Player class
                self.head = self.head.next
        if not forward:
            while self.tail:
                print(self.tail.player)
                self.tail = self.tail.previous

    def find(self, key_to_find):
        if self.is_empty():
            return None
        current_node = self._head
        while current_node:
            if current_node.key == key_to_find:
                return current_node.player
            current_node = current_node.next
        return None

    def __len__(self):
        current_node = self._head
        counter = 0
        while current_node:
            counter += 1
            current_node = current_node.next
        return counter

    def __iter__(self):
        current_node = self._head
        while current_node:
            yield current_node.player #yeild acts like return but pauses and resumes instead of exiting
            current_node = current_node.next

    @property
    def head(self): #for accessing the private head
        return self._head

    @head.setter # setter function to allow assigning _head to something
    def head(self, player_node):
        self._head = player_node

    @property
    def tail(self): #for accessing the private tail
        return self._tail

    @tail.setter
    def tail(self,player_node):
        self._tail = player_node


