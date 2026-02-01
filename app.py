import time
import random
import datetime

print("--- Starting Offline Data Automation ---")

users = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
actions = ["Login", "Purchase", "Logout", "Upload", "Download"]

while True:
    # 1. Simulate fetching data
    current_user = random.choice(users)
    current_action = random.choice(actions)
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    
    # 2. Simulate processing (The "Automation")
    log_message = f"[{timestamp}] User: {current_user} | Action: {current_action}"
    
    # 3. Log the output
    print(log_message)
    
    # 4. Wait 5 seconds
    time.sleep(5)