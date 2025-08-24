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
        self.assertEqual(sut.tail.player.uid, "01") #tail should be the same as head

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
        self.assertEqual(sut.tail.player.uid, "02")

    def test_insert_tail_empty_list(self):
        sut = PlayerList()
        self.assertTrue(sut.is_empty())  # list should be empty at this point

        player = Player("04", "JimmyBillBob")
        node = PlayerNode(player)
        sut.insert_tail(node)

        self.assertFalse(sut.is_empty())

        #head and tail should be the same
        self.assertEqual(sut.head.player.uid, "04")
        self.assertEqual(sut.tail.player.uid, "04")

        #nothing should be on either side of head(tail)
        self.assertIsNone(sut.head.previous)
        self.assertIsNone(sut.head.next)
        self.assertIsNone(sut.tail.previous)
        self.assertIsNone(sut.tail.next)

    def test_insert_tail_not_empty_list(self):
        sut = PlayerList()
        self.assertTrue(sut.is_empty())  # list should be empty at this point

        # create 2 players
        player1= Player("05", "MilesDavis")
        player2 = Player("06", "KiloMetersDavis")

        # create 2 nodes out of the 2 players
        node1 = PlayerNode(player1)
        node2 = PlayerNode(player2)

        # insert the 2 nodes
        sut.insert_tail(node1)
        sut.insert_tail(node2)

        #node1 shoudl be head and node2 should be tail
        self.assertEqual(sut.head.player.uid, "05")
        self.assertEqual(sut.tail.player.uid, "06")

        #head's next should be tail and tail's previous should be head
        self.assertEqual(sut.head.next.player.uid, "06")
        self.assertEqual(sut.tail.previous.player.uid, "05")

        #nothing should be in front of head and nothing should behind tail
        self.assertIsNone(sut.head.previous)
        self.assertIsNone(sut.tail.next)


if __name__ == "__main__":
    unittest.main()

