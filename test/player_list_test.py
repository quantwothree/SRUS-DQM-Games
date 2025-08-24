import unittest
from app.player import Player
from app.player_node import PlayerNode
from app.player_list import PlayerList

class TestPlayerList(unittest.TestCase):
    def test_insert_head_empty_list(self):
        sut = PlayerList()
        self.assertTrue(sut.is_empty()) #list should be empty at this point

        player = Player("01", "AliceInWonderland")
        node = PlayerNode(player)
        sut.insert_head(node)

        self.assertFalse(sut.is_empty()) #list should not be empty after insert a node
        self.assertEqual(sut.head.player.uid, "01")
        self.assertIsNone(sut.head.previous) #if list was empty then nothing should be on either side of head
        self.assertIsNone(sut.head.next)

    def test_insert_head_not_empty_list(self):
        sut = PlayerList()
        self.assertTrue(sut.is_empty())  # list should be empty at this point

        #create 2 players
        player = Player("02", "BillShakespeare")
        player2 = Player("03", "WilliamShakespeare")

        #create 2 nodes out of the 2 players
        node = PlayerNode(player)
        node2 = PlayerNode(player2)

        #insert the 2 nodes
        sut.insert_head(node)
        sut.insert_head(node2)

        self.assertFalse(sut.is_empty()) #list should not be empty after insert the nodes

        self.assertEqual(sut.head.player.uid, "03")
        self.assertEqual(sut.head.next.player.uid, node.player.uid)
        self.assertIsNone(sut.head.previous)

if __name__ == "__main__":
    unittest.main()

