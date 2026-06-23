import unittest
from delivery_routing import minDeliveryTime

class TestDeliveryRouting(unittest.TestCase):
    def test_basic_path(self):
        # Can reach without chargers
        grid = [
            ['S', '0', '0'],
            ['1', '1', '0'],
            ['0', '0', 'D']
        ]
        self.assertEqual(minDeliveryTime(grid, 5), 4)

    def test_needs_charger(self):
        # B=2. S -> 0 is 1 step, battery=1. 0 -> C is 1 step, battery=2.
        # C -> 0 -> D is 2 steps. Total 4 steps.
        # If we didn't have C, we would run out of battery.
        grid = [
            ['S', '0', 'C'],
            ['1', '1', '0'],
            ['D', '0', '0']
        ]
        self.assertEqual(minDeliveryTime(grid, 2), 4)

    def test_revisit_cell(self):
        # THE TWIST: Must revisit a cell.
        # S(0,0)->(0,1)->C(0,2) recharges. 
        # Then goes back through (0,1)->(1,1)->(2,1)->D(2,0)
        grid = [
            ['S', '0', 'C'],
            ['1', '0', '1'],
            ['D', '0', '1']
        ]
        # Requires exact management of state to allow revisiting (0,1)
        self.assertEqual(minDeliveryTime(grid, 4), 6)

    def test_impossible(self):
        grid = [
            ['S', '0', '0'],
            ['1', '1', '1'],
            ['D', '0', '0']
        ]
        self.assertEqual(minDeliveryTime(grid, 10), -1)

if __name__ == '__main__':
    unittest.main()
