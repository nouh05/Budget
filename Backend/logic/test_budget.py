import unittest
from Backend.logic.budget import calculate_budget, calculate_return

class TestBudgetFunctions(unittest.TestCase):
    def test_calculate_budget_moderate(self):
        user = {"monthly_income": 5000, "strategy": "moderate"}
        result = calculate_budget(user)
        self.assertEqual(result, {"needs": 2500, "wants": 1500, "invest_pct": 1000})
    
    def test_calculate_budget_aggressive(self):
        user = {"monthly_income": 5000, "strategy": "aggressive"}
        result = calculate_budget(user)
        self.assertEqual(result, {"needs": 2500, "wants": 1000, "invest_pct": 1500})
    
    def test_calculate_return(self):
        result = calculate_return(500, 25, 65)
        self.assertTrue(result > 0)
    
        
    if __name__ == '__main__':
        unittest.main()