class MonetizationEngine:

    def __init__(self, game_engine):
        self.game = game_engine

    def trigger_rewarded_ad(self, placement_type):
        """Simulate watching a rewarded ad based on placement type."""
        print(f"\n[Monetization] Ad Triggered: {placement_type}")

        if placement_type == "offline_double":
            self.game.apply_multiplier(2.0)
            print("[Monetization] Reward Granted: 2x Boost applied!")
            return True

        print("[Monetization] Ad failed or skipped.")
        return False
      
