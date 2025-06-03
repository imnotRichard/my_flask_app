import unittest
from src.app import calc_health_score

class TestHealthScore(unittest.TestCase):
    def test_excellent(self):
        # 8 hours of sleep, 2000ml water intake
        self.assertEqual(calc_health_score(8, 2000), 100)
    def test_normal(self):
        # 7 hours of sleep, 1200ml water intake
        self.assertEqual(calc_health_score(7, 1200), 60)
    def test_bad(self):
        # 5 hours of sleep, 500ml water intake
        self.assertEqual(calc_health_score(5, 500), 20)
    def test_invalid_input(self):
        # Invalid input
        self.assertEqual(calc_health_score("abc", "xyz"), 0)

if __name__ == '__main__':
    unittest.main()
