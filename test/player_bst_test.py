import unittest
from player import Player
from player_bnode import PlayerBNode
from player_bst import PlayerBST

class TestPlayerBSTInsert(unittest.TestCase):

    def test_insert_empty_tree(self):
        bst = PlayerBST(None)
        player = Player("1", "Alean", 100)
        bst.insert(player)

        self.assertEqual(bst.root.player.name, "Alean")
        self.assertIsNone(bst.root.left_bnode)
        self.assertIsNone(bst.root.right_bnode)

    def test_insert_multiple_nodes(self):
        bst = PlayerBST(None)

        players = [
            Player("1", "Dean", 100),
            Player("2", "Bean", 50),
            Player("3", "Frean", 75),
            Player("4", "Alean", 25),
            Player("5", "Chean", 60)
        ]

        for player in players:
            bst.insert(player)

        self.assertEqual(bst.root.player.name, "Dean")
        self.assertEqual(bst.root.left_bnode.player.name, "Bean")
        self.assertEqual(bst.root.right_bnode.player.name, "Frean")
        self.assertEqual(bst.root.left_bnode.left_bnode.player.name, "Alean")
        self.assertEqual(bst.root.left_bnode.right_bnode.player.name, "Chean")

    def test_insert_duplicate_root(self):
        bst = PlayerBST(None)

        player1 = Player("1", "Alice", 100)
        player2 = Player("2", "Alice", 200)
        bst.insert(player1)
        bst.insert(player2)

        self.assertEqual(bst.root.player.uid, "2")

    def test_insert_duplicate_deep(self):
        bst = PlayerBST(None)

        players = [
            Player("1", "Dean", 100),
            Player("2", "Bean", 50),
            Player("3", "Frean", 75),
            Player("4", "Alean", 25),
            Player("5", "Chean", 60),
            Player("6", "Alean", 80),
        ]

        for player in players:
            bst.insert(player)

        #Checks if Alean is now the new Alean
        self.assertEqual(bst.root.left_bnode.left_bnode.player.uid,"6")
        self.assertEqual(bst.root.left_bnode.left_bnode.player.score, 80)


if __name__ == '__main__':
    unittest.main()

