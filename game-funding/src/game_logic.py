class GameEngine:

    def __init__(self):
        self.balance = 0.0
        self.base_income_rate = 10.0
        self.multiplier = 1.0

    def update(self):
        """Simulate a single time tick in the game."""
        generated = self.base_income_rate * self.multiplier
        self.balance += generated
        return self.balance

    def apply_multiplier(self, value):
        """Apply a temporary or permanent income multiplier."""
        self.multiplier *= value
        print(f"[GameEngine] Multiplier updated to {self.multiplier}x")
      
