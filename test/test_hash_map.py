import unittest
from player import Player
from hash_map import HashMap
from player_list import KeyNotFoundException

class TestHashMap(unittest.TestCase):
    def setUp(self):
        self.hash_map = HashMap(5)

    def test_setitem_and_getitem(self):
        self.hash_map["01"] = "Saul Goodman"
        self.hash_map["02"] = "Kim Wexler"

        player1 = self.hash_map["01"]
        player2 = self.hash_map["02"]

        self.assertEqual(player1.uid, "01")
        self.assertEqual(player1.name, "Saul Goodman")
        self.assertEqual(player2.uid, "02")
        self.assertEqual(player2.name, "Kim Wexler")

    #test to see if __getitem__ works with a Player object
    def test_getitem_with_player_object(self):
        self.hash_map["01"] = "Saul Goodman"
        player = Player("01", "FakeName")
        #getting the player with id 01
        self.assertEqual(self.hash_map[player].name, "Saul Goodman")

    def test_setitem_with_player_object(self):
        player = Player("01", "Saul Goodman")
        self.hash_map[player] = "Jimmy McGill"  # should update name
        self.assertEqual(self.hash_map["01"].name, "Jimmy McGill")

    def test_changing_player_name(self):
        self.hash_map["01"] = "Saul Goodman"
        self.hash_map["01"] = "Jimmy McGill"

        player = self.hash_map["01"]
        self.assertEqual(player.name, "Jimmy McGill")

    def test_get_index(self):
        index1 = self.hash_map.get_index("01")
        index2 = self.hash_map.get_index("01")
        index3 = self.hash_map.get_index("02")

        self.assertIsInstance(index1, int)
        self.assertEqual(index1, index2)
        self.assertGreaterEqual(index1, 0) #index should be from 0 to 9
        self.assertLess(index1, self.hash_map.size)

        #test using a Player object
        player1 = Player("03", "Mike Ehrmantraut")
        player2 = Player("03", "Howard Hemlin")
        index1 = self.hash_map.get_index(player1)
        index2 = self.hash_map.get_index(player2)
        self.assertEqual(index1, index2)
        self.assertIsInstance(index1, int)
        self.assertGreaterEqual(index1, 0)
        self.assertLess(index1, self.hash_map.size)

    def test_delitem(self):
        self.hash_map["01"] = "Saul Goodman"
        self.hash_map["02"] = "Kim Wexler"
        self.assertEqual(len(self.hash_map), 2)

        del self.hash_map["01"]
        del self.hash_map["02"]
        self.assertEqual(len(self.hash_map), 0)  # Expecting 0 players left

        #test __delitem__ if Player was not found
        self.hash_map["01"] = "Saul Goodman"
        del self.hash_map["01"]
        with self.assertRaises(KeyNotFoundException) as error:
            del self.hash_map["01"] #nothing left to delete so exception should be raised
        self.assertEqual(type(error.exception), KeyNotFoundException)

    def test_len(self):
        self.assertEqual(len(self.hash_map), 0)

        self.hash_map["01"] = "Saul Goodman"
        self.hash_map["02"] = "Kim Wexler"
        self.assertEqual(len(self.hash_map), 2)

        del self.hash_map["01"]
        self.assertEqual(len(self.hash_map), 1)

    def test_display(self):
        #For manual inspection, not assertions
        self.hash_map["01"] = "Saul Goodman"
        self.hash_map["02"] = "Kim Wexler"
        self.hash_map["03"] = "Mike Ehrmantraut"

        print("HashMap: ")
        self.hash_map.display()

if __name__ == "__main__":
    unittest.main()
