class AuthManager:

    def __init__(self):
        self.user_id = None
        self.is_authenticated = False
        self.is_online = False

    def check_network_status(self, is_connected: bool):
        """تحديث حالة الاتصال للتبديل بين وضع الأوفلاين والأونلاين."""
        self.is_online = is_connected
        status = "Online" if self.is_online else "Offline"
        print(f"[Auth] Network status updated: {status}")

    def login_guest(self):
        """تسجيل دخول محلي كضيف للعمل في وضع الأوفلاين."""
        self.user_id = "guest_local_user"
        self.is_authenticated = True
        print("[Auth] Logged in as Local Guest (Offline Mode).")
        return True

    def login_with_provider(self, provider_name, token):
        """تسجيل الدخول عبر Google/Apple عند توفر الإنترنت."""
        if not self.is_online:
            print("[Auth Error] Internet connection required for cloud login.")
            return self.login_guest()

        if token:
            self.user_id = f"{provider_name}_user_12345"
            self.is_authenticated = True
            print(
                f"[Auth Success] Logged in via {provider_name}. Cloud sync enabled."
            )
            return True

        return False
      
