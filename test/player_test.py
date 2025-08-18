import unittest
from app.player import Player #app.player tells it where to find player.py

class TestPlayer(unittest.TestCase):
    def test_uid(self):
        player = Player("01", "Alice")
        self.assertEqual(player.uid, "01")

    def test_name(self):
        player = Player("02", "Bob")
        self.assertEqual(player.name, "Bob")

if __name__ == "__main__":
    unittest.main()
