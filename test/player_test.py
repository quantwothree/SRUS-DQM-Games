import unittest
import random
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

    def test_custom_sort(self):
        players = [Player('01', "Alice", 10), Player('02', "Bob", 5), Player('03', "Charlie", 15)]
        players_manually_sorted = [Player('03', "Charlie", 15), Player('01', "Alice", 10), Player('02', "Bob", 5)]
        players_sorted = Player.custom_sort(players)
        self.assertListEqual(players_sorted, players_manually_sorted)

    def test_custom_sort_at_large_scale(self):
        players = [Player(f"{i:03}", f"Player {i}",random.randint(0, 1000)) for i in range(1000)]
        players_manually_sorted = sorted(players, reverse=True)
        players_sorted = Player.custom_sort(players)
        self.assertListEqual(players_manually_sorted,players_sorted)

    def test_custom_sort_on_sorted_list(self):
        players_unsorted = [Player(f"{i:03}", f"Player {i}", random.randint(0, 1000)) for i in range(1000)]
        players_sorted = sorted(players_unsorted, reverse=True)

        #sorting an unsorted list
        players_custom_sorted_from_unsorted = Player.custom_sort(players_unsorted)
        #sorting a sorted list
        players_custom_sorted_from_sorted = Player.custom_sort(players_sorted)

        self.assertListEqual(players_custom_sorted_from_unsorted,players_custom_sorted_from_sorted)


if __name__ == "__main__":
    unittest.main()
