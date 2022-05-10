import unittest
from funcs import *

# here is a sample puzzle for you to use in your tests
puzzle = ["WAQHGTTWEE",
          "CBMIVQQELS",
          "AZXWKWIIIL",
          "LDWLFXPIPV",
          "PONDTMVAMN",
          "OEDSOYQGOB",
          "LGQCKGMMCT",
          "YCSLOACUZM",
          "XVDMGSXCYZ",
          "UUIUNIXFNU"]

puzzle1 = 'WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU'
puzzle2 = 'EOARBRNIABZEBRAEBRBHARRACCOONRAACBRRCHECCNABOZOBKABONIRBBNCAEERTCBRAIAABCERICRHRBOIORORCCOBOAAKRKEAR'
		  
class TestCases(unittest.TestCase):
   def test_check_forward_1(self):
      word = "UNIX"
      self.assertEqual(checkForward(puzzle1, word), 'UNIX: (FORWARD) row: 9 column: 3')
   # add your tests here
   def test_check_forward_2(self):
      word = "ZEBRA"
      self.assertEqual(checkForward(puzzle2, word), 'ZEBRA: (FORWARD) row: 1 column: 0')
   def test_check_forward_3(self):
      word = "BEAR"
      self.assertEqual(checkForward(puzzle2, word), None)
   def test_check_backword_1(self):
      word = "VIM"
      self.assertEqual(checkBackward(puzzle1, word), 'VIM: (BACKWARD) row: 1 column: 4')
   def test_check_backword_2(self):
      word = "BEAR"
      self.assertEqual(checkBackward(puzzle2, word), 'BEAR: (BACKWARD) row: 1 column: 6')
   def test_check_backword_3(self):
      word = "CPE"
      self.assertEqual(checkBackward(puzzle2, word), None)
   def test_check_up_1(self):
      word = "CHICKEN"
      self.assertEqual(checkUp(puzzle2, word), 'CHICKEN: (UP) row: 8 column: 8')
   def test_check_up_2(self):
      word = "COMPILE"
      self.assertEqual(checkUp(puzzle1, word), 'COMPILE: (UP) row: 6 column: 8')
   def test_check_up_3(self):
      word = "CHICKEN"
      self.assertEqual(checkUp(puzzle1, word), None)
   def test_check_down_1(self):
      word = "RABBIT"
      self.assertEqual(checkDown(puzzle2, word), 'RABBIT: (DOWN) row: 1 column: 3')
   def test_check_down_2(self):
      word = "CALPOLY"
      self.assertEqual(checkDown(puzzle1, word), 'CALPOLY: (DOWN) row: 1 column: 0')
   def test_check_down_3(self):
      word = "CPE"
      self.assertEqual(checkDown(puzzle1, word), None)
   def test_check_diagonal_1(self):
      word = "VIM"
      self.assertEqual(checkDiagonal(puzzle1, word), None) 
   def test_check_diagonal_2(self):
      word = "GCC"
      self.assertEqual(checkDiagonal(puzzle1, word), 'GCC: (DIAGONAL) row: 6 column: 5') 
   def test_check_diagonal_3(self):
      word = "CPE"
      self.assertEqual(checkDiagonal(puzzle1, word), 'CPE: (DIAGONAL) row: 1 column: 0')

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

