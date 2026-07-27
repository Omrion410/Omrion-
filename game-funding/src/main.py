import time
from game_logic import GameEngine
from monetization_engine import MonetizationEngine


def main():
    print("=== Initializing Game Funding Project ===")
    game = GameEngine()
    monetization = MonetizationEngine(game)

    # Simulation cycle
    for tick in range(1, 6):
        time.sleep(0.5)
        game.update()
        print(
            f"[Tick {tick}] Balance: {game.balance:.2f} | Multiplier: {game.multiplier}x"
        )

        if tick == 3:
            monetization.trigger_rewarded_ad("offline_double")

    print("\nSimulation complete. Final Balance:", round(game.balance, 2))


if __name__ == "__main__":
    main()
  
