import hashlib
import json


class SecurityManager:

    def __init__(self, secret_key="GameFundingSecureKey2026"):
        self.secret_key = secret_key

    def generate_hash(self, data_dict):
        """توليد التوقيع الرقمي لمنع التعديل على بيانات اللاعب أوفلاين."""
        data_string = (
            json.dumps(data_dict, sort_keys=True) + self.secret_key
        )
        return hashlib.sha256(data_string.encode("utf-8")).hexdigest()

    def verify_data(self, data_dict, provided_hash):
        """التحقق من صحة البيانات وعدم تلغيمها أو تعديلها."""
        calculated_hash = self.generate_hash(data_dict)
        return calculated_hash == provided_hash

    def encrypt_offline_save(self, player_data):
        """تجهيز البيانات مع التوقيع الرقمي للحفظ الآمن."""
        save_hash = self.generate_hash(player_data)
        return {"data": player_data, "hash": save_hash}
      
