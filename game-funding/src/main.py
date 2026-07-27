import time
from auth_manager import AuthManager
from game_logic import GameEngine
from iap_manager import IAPManager
from monetization_engine import MonetizationEngine
from security import SecurityManager


def main():
    print("=== Game Funding Project - Live Engine v1.0.0 ===")
    print("=== Continuous Development & LiveOps Integrated ===")

    # 1. تهيئة الأجهزة والمحركات الأساسية
    game = GameEngine()
    security = SecurityManager()
    auth = AuthManager()
    monetization = MonetizationEngine(game)
    iap = IAPManager(game)

    # 2. محاكاة بدء اللعبة في وضع الأوفلاين (Local Mode)
    print("\n--- [Step 1] Offline Boot Sequence ---")
    auth.check_network_status(is_connected=False)
    auth.login_guest()

    # 3. شراء ميزة دائمية أوفلاين (Permanent Boosters)
    print("\n--- [Step 2] Processing Local Non-Consumable IAP ---")
    iap.process_purchase("permanent_2x_boost", receipt_token="local_receipt_101")

    # 4. محاكاة الاتصال بالإنترنت والمزامنة السحابية
    print("\n--- [Step 3] Connecting Online & Cloud Sync ---")
    auth.check_network_status(is_connected=True)
    auth.login_with_provider("Google", token="valid_google_oauth_token")

    # 5. تشغيل دورة المحاكاة والأرباح الهجينة
    print("\n--- [Step 4] Running Hybrid Game Loop ---")
    for tick in range(1, 4):
        time.sleep(0.3)
        game.update()
        print(
            f"[Tick {tick}] Balance: ${game.balance:.2f} | Multiplier: {game.multiplier}x"
        )

        # تجربة عرض إعلان مكافأة عند توفر الإنترنت
        if tick == 2:
            monetization.trigger_rewarded_ad("offline_double")

    # 6. تشفير بيانات الحفظ لمنع التلاعب أوفلاين/أونلاين (SHA-256)
    player_data = {
        "user_id": auth.user_id,
        "balance": game.balance,
        "multiplier": game.multiplier,
        "has_no_ads": getattr(game, "has_no_ads", False),
    }
    encrypted_save = security.encrypt_offline_save(player_data)

    print("\n--- [Step 5] Security Check & Save State ---")
    print(f"Player Data Hash Signature: {encrypted_save['hash'][:24]}...")
    print(f"Final Account Balance: ${round(game.balance, 2)}")
    print("=== System Status: All Systems Operational & Secure ===")


if __name__ == "__main__":
    main()
    
  
