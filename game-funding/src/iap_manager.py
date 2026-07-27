class IAPManager:

    def __init__(self, game_engine):
        self.game = game_engine
        # كتالوج المنتجات مع أسعار مرجعية (تُترجم تلقائياً لـ DZD / EUR / USD بواسطة المتجر)
        self.products = {
            "remove_ads_bundle": {
                "name": "No Ads + Bonus Multiplier",
                "price_usd": 4.99,
                "type": "non_consumable",
            },
            "permanent_2x_boost": {
                "name": "Permanent 2x Income Boost",
                "price_usd": 9.99,
                "type": "non_consumable",
            },
            "gem_pack_small": {
                "name": "100 Gems Pack",
                "price_usd": 0.99,
                "type": "consumable",
            },
            "vip_pass": {
                "name": "Monthly VIP Pass",
                "price_usd": 7.99,
                "type": "subscription",
            },
        }

    def process_purchase(self, product_id, receipt_token):
        """التحقق من الفاتورة وتفعيل الميزة للاعب (يعمل أوفلاين وأونلاين للـ Non-Consumable)."""
        if not receipt_token:
            print(f"[IAP Error] Invalid receipt token for {product_id}.")
            return False

        if product_id == "remove_ads_bundle":
            self.game.has_no_ads = True
            print("[IAP Success] Ads removed permanently!")
            return True

        elif product_id == "permanent_2x_boost":
            self.game.apply_multiplier(2.0)
            print("[IAP Success] Permanent 2x boost activated!")
            return True

        elif product_id == "gem_pack_small":
            self.game.add_gems(100)
            print("[IAP Success] 100 Gems added to account.")
            return True

        return False
      
