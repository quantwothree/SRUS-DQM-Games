import unittest
from app.player import Player #app.player tells it where to find player.py

class TestPlayer(unittest.TestCase):
    def test_uid(self):
        player = Player("01", "Alice")
        self.assertEqual(player.uid, "01")

    def test_name(self):
        player = Player("02", "Bob")
        self.assertEqual(player.name, "Bob")

    def test_sort_players(self):
        players = [Player('01',"Alice", 10), Player('02',"Bob",5),
                   Player('03', "Charlie", 15)]

        # do **not** change the following code:
        sorted_players = sorted(players)

        # players must be sorted by score as shown here:
        manually_sorted_players = [Player('02',"Bob", 5), Player('01', "Alice", 10),
                                   Player('03', "Charlie", 15)]

        self.assertListEqual(sorted_players, manually_sorted_players)

    def test_players_can_be_compared_by_score(self):

        alice = Player('01', "Alice", 10)
        bob = Player('02', "Bob", 5)

        self.assertLess(bob, alice)

if __name__ == "__main__":
    unittest.main()
