import requests
from src.config import REGISTER_DEVICE_URL, REFRESH_TOKEN_URL, ONE_TIME_CODE, DEVICE_DESC, DEVICE_ID

class reMarkable:
    def __init__(self, device_token=None, user_token=None):
        """Args:
            device_token (str): The device token.
            user_token (str): The user token."""
            
        self.device_token = device_token  # Store the device token separately
        self.user_token = user_token  # Store the user token separately


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
        

    def test_auth(self):
        """Test the authentication by fetching the user info and listing documents."""
        if not self.user_token:
            raise Exception("❌ No user token found. Please authenticate first.")

        response = requests.get(
            "https://webapp.cloud.remarkable.com/document-storage/json/2/docs",
            headers={"Authorization": f"Bearer {self.user_token}"}
        )

        if response.status_code == 200:
            documents = response.json()  # List of documents
            print(f"✅ Authentication successful! Found {len(documents)} documents.")

            for doc in documents:
                print(f"- {doc['VissibleName']} (ID: {doc['ID']}, Type: {doc['Type']})")
        else:
            raise Exception("❌ Authentication failed:", response.status_code)






