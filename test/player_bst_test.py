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

    def test_search(self):
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

        #Find Dean - Which is also the root
        result = bst.search("Dean")
        self.assertEqual(result, players[0])
        self.assertEqual(result.uid, players[0].uid)
        self.assertEqual(result.score, players[0].score)

        # Find Bean
        result = bst.search("Bean")
        self.assertEqual(result, players[1])
        self.assertEqual(result.uid, players[1].uid)
        self.assertEqual(result.score, players[1].score)

        # Find Frean
        result = bst.search("Frean")
        self.assertEqual(result, players[2])
        self.assertEqual(result.uid, players[2].uid)
        self.assertEqual(result.score, players[2].score)

        # Find Alean (should be at index 5 since index 3 Alean got replaced)
        result = bst.search("Alean")
        self.assertEqual(result, players[5])
        self.assertEqual(result.uid, players[5].uid)
        self.assertEqual(result.score, players[5].score)

        # Find Chean
        result = bst.search("Chean")
        self.assertEqual(result, players[4])
        self.assertEqual(result.uid, players[4].uid)
        self.assertEqual(result.score, players[4].score)

        # Search for non-existent player
        result = bst.search("Pean")
        self.assertIsNone(result)

    def test_search_with_empty_tree(self):
        bst = PlayerBST(None)
        result = bst.search("someone")
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()

