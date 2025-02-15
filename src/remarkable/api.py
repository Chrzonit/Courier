import requests
from src.config import REGISTER_DEVICE_URL, REFRESH_TOKEN_URL, ONE_TIME_CODE, DEVICE_DESC, DEVICE_ID

class reMarkable:
    def __init__(self):
        self.device_token = None
        self.user_token = None  # Store the user token separately

    def get_device_token(self):
        """Registers a new device and retrieves a device token."""
        payload = {
            "code": ONE_TIME_CODE,
            "deviceDesc": DEVICE_DESC,
            "deviceID": DEVICE_ID
        }

        response = requests.post(REGISTER_DEVICE_URL, json=payload, headers={"Authorization": "Bearer"})

        if response.status_code == 200:
            self.device_token = response.text.strip()
            print("✅ Device token received:", self.device_token)
            return self.device_token
        else:
            raise Exception("❌ Authentication failed:", response.status_code, response.text)

    def refresh_user_token(self):
        """Refreshes the user token using the device token."""
        if not self.device_token:
            raise Exception("❌ No device token found. Please authenticate first.")

        response = requests.post(
            REFRESH_TOKEN_URL,
            headers={"Authorization": f"Bearer {self.device_token}"}
        )

        if response.status_code == 200:
            self.user_token = response.text.strip()
            print("🔄 User token refreshed successfully:", self.user_token)
            return self.user_token
        else:
            raise Exception("❌ Token refresh failed:", response.status_code, response.text)

# Usage
rm = reMarkable()
device_token = rm.get_device_token()
user_token = rm.refresh_user_token()

with open("device_token.txt", "w") as file:
    file.write(device_token)

with open("user_token.txt", "w") as file:
    file.write(user_token)


