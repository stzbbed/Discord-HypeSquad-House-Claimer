import requests
import getpass
import time

API_URL = "https://discord.com/api/v9/hypesquad/online"

houses = {
    "1": "Bravery",
    "2": "Brilliance",
    "3": "Balance"
}


print("""
========================================
    Discord HypeSquad House Selector
========================================

        Made by stzbbed on Github
           All rights reserved.

========================================
""")

for house_id, name in houses.items():
    print(f"{house_id}. {name}")


choice = input("\nChoose your house (1/2/3): ")

if choice not in houses:
    print("Invalid house selection.")
    raise SystemExit

token = getpass.getpass("Discord authorization token: ")

response = requests.post(
    API_URL,
    headers={
        "Authorization": token,
        "Content-Type": "application/json"
    },
    json={"house_id": int(choice)},
    timeout=15
)

if response.status_code == 204:
    print(f"Success! Request accepted for {houses[choice]}.")
elif response.status_code == 401:
    print("Authentication failed.")
elif response.status_code == 403:
    print("Discord rejected the request.")
else:
    print(f"Request failed: HTTP {response.status_code}")
    print(response.text[:300])

print("\nClosing in 3 seconds...")
time.sleep(3)


# Discord HypeSquad House Selector
# Copyright (c) 2026 stzbbed
# All rights reserved.
#
# Unauthorized copying, redistribution, or
# claiming this code as your own is prohibited.
