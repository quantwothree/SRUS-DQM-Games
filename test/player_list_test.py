import unittest
from app.player import Player
from app.player_node import PlayerNode
from app.player_list import PlayerList, EmptyListException, KeyNotFoundException

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

    def test_delete_at_head(self):
        #for when list is empty
        sut = PlayerList()
        self.assertTrue(sut.is_empty())

        with self.assertRaises(EmptyListException) as error:
            sut.delete_at_head()
        self.assertEqual(type(error.exception), EmptyListException)
        # check if the message is exactly the same
        self.assertEqual(error.exception.args[0], "Can not delete from an empty list")

        #now add 1 node to the empty list
        player1 = Player("08", "SaulGoodman")
        node1 = PlayerNode(player1)
        sut.insert_head(node1)

        self.assertFalse(sut.is_empty())
        sut.delete_at_head()

        self.assertTrue(sut.is_empty())
        self.assertIsNone((sut.head), None)
        self.assertIsNone((sut.tail), None)

        #add 2 nodes to the list
        player1 = Player("08", "SaulGoodman")
        node1 = PlayerNode(player1)
        sut.insert_head(node1)

        player2 = Player("09", "KimWexler")
        node2 = PlayerNode(player2)
        sut.insert_head(node2)

        self.assertFalse(sut.is_empty())
        sut.delete_at_head()
        self.assertEqual(sut.head.player.uid, "08")
        self.assertIsNone(sut.head.previous, None)

    def test_delete_at_tail(self):
        # for when list is empty
        sut = PlayerList()
        self.assertTrue(sut.is_empty())

        with self.assertRaises(EmptyListException) as error:
            sut.delete_at_tail()
        self.assertEqual(type(error.exception), EmptyListException)
        # check if the message is exactly the same
        self.assertEqual(error.exception.args[0], "Can not delete from an empty list")

        # now add 1 node to the empty list
        player1 = Player("08", "SaulGoodman")
        node1 = PlayerNode(player1)
        sut.insert_head(node1)

        self.assertFalse(sut.is_empty())
        sut.delete_at_tail()

        self.assertTrue(sut.is_empty())
        self.assertIsNone((sut.head), None)
        self.assertIsNone((sut.tail), None)

        # add 2 nodes to the list
        player1 = Player("08", "SaulGoodman")
        node1 = PlayerNode(player1)
        sut.insert_head(node1)

        player2 = Player("09", "KimWexler")
        node2 = PlayerNode(player2)
        sut.insert_head(node2)

        self.assertFalse(sut.is_empty())
        sut.delete_at_tail()

        self.assertEqual(sut.tail.player.uid, "09")
        self.assertIsNone(sut.tail.next, None)

    def test_delete_at_key(self):
        # for when list is empty
        sut = PlayerList()
        self.assertTrue(sut.is_empty())

        with self.assertRaises(EmptyListException) as error:
            sut.delete_at_key("03")
        self.assertEqual(type(error.exception), EmptyListException)
        self.assertEqual(error.exception.args[0], "Can not delete from an empty list")

        # Add 1 node and check with valid / unvalid key
        player1 = Player("01", "SaulGoodman")
        node1 = PlayerNode(player1)
        sut.insert_head(node1)

        with self.assertRaises(KeyNotFoundException) as error:
            sut.delete_at_key("03")
        self.assertEqual(type(error.exception), KeyNotFoundException)
        self.assertEqual(error.exception.args[0], "Can not find key in list")

        sut.delete_at_key("01")
        self.assertTrue(sut.is_empty())

        # Add 4 nodes
        player1 = Player("01", "SaulGoodman")
        node1 = PlayerNode(player1)
        sut.insert_head(node1)

        player2 = Player("02", "KimWexler")
        node2 = PlayerNode(player2)
        sut.insert_head(node2)

        player3 = Player("03", "Chuck McGill")
        node3 = PlayerNode(player3)
        sut.insert_head(node3)

        player4 = Player("04", "Lalo Salamanca")
        node4 = PlayerNode(player4)
        sut.insert_head(node4)

        # The list is now 4,3,2,1
        with self.assertRaises(KeyNotFoundException) as error:
            sut.delete_at_key("05")
        self.assertEqual(type(error.exception), KeyNotFoundException)
        self.assertEqual(error.exception.args[0], "Can not find key in list")

        sut.delete_at_key("03")
        self.assertEqual(sut.tail.previous.player.uid, "02")
        sut.delete_at_key("02")
        self.assertEqual(sut.head.next.player.uid, "01")

if __name__ == "__main__":
    unittest.main()

