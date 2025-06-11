import unittest
import sys
sys.path.append('../game')

from board import Board
from district import District

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board(players=2)

    def test_board_initialization(self):
        self.assertIsNotNone(self.board.combat_upgrade_market)
        self.assertIsNotNone(self.board.edgerunners_market)
        self.assertIsNotNone(self.board.opportunities_market)
        self.assertIsNotNone(self.board.the_net)
        
        self.assertEqual(len(self.board.districts), 6)
        self.assertIn("City Center", self.board.districts)
        self.assertIn("Heywood", self.board.districts)
        self.assertIn("Pacifica", self.board.districts)
        self.assertIn("Santo Domingo", self.board.districts)
        self.assertIn("Watson", self.board.districts)
        self.assertIn("Westbrook", self.board.districts)

    def test_district_neighbors(self):
        self.assertEqual(self.board.neighbors["City Center"], 
                        {"Heywood", "Watson", "Westbrook"})
        self.assertEqual(self.board.neighbors["Pacifica"],
                        {"Heywood", "Santo Domingo"})
        
        for district, neighbors in self.board.neighbors.items():
            for neighbor in neighbors:
                self.assertIn(district, self.board.neighbors[neighbor],
                             f"{district} should be a neighbor of {neighbor}")

    def test_districts_are_district_objects(self):
        for name, district in self.board.districts.items():
            self.assertIsInstance(district, District)
            self.assertEqual(district.name, name)

if __name__ == '__main__':
    unittest.main()