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
        # B=4.
        # S(0,0) -> 0(0,1) -> C(0,2) takes 2 steps. Battery becomes 4.
        # C(0,2) -> 0(1,2) -> 0(2,2) -> 0(2,1) -> D(2,0) takes 4 steps.
        # Total 6 steps.
        # If we didn't have C, we would run out of battery (path is 6 steps, B is 4).
        grid = [
            ['S', '0', 'C'],
            ['1', '1', '0'],
            ['D', '0', '0']
        ]
        self.assertEqual(minDeliveryTime(grid, 4), 6)

    def test_revisit_cell(self):
        # THE TWIST: Must revisit a cell.
        # Direct path S to D takes 4 steps. B=3, so you will run out of battery.
        # You MUST detour into the dead-end to hit C, recharge, and walk back out.
        grid = [
            ['S', '0', '0', '0', 'D'],
            ['1', '1', 'C', '1', '1']
        ]
        # Path: S(0,0)->(0,1)->(0,2)->C(1,2) [recharges to 3] -> (0,2) [revisited!] -> (0,3) -> D(0,4)
        # Total steps: 6
        self.assertEqual(minDeliveryTime(grid, 3), 6)

    def test_impossible(self):
        grid = [
            ['S', '0', '0'],
            ['1', '1', '1'],
            ['D', '0', '0']
        ]
        self.assertEqual(minDeliveryTime(grid, 10), -1)

if __name__ == '__main__':
    unittest.main()
