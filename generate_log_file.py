import random
from datetime import datetime, timedelta

# Create a sample log file with 1000 entries
log_entries = []
start_time = datetime(2024, 8, 4, 10, 0, 0)

users = ["User1", "User2", "User3", "User4", "User5", "User6", "User7", "User8"]
events = ["logged in", "accessed file secret.txt", "accessed file public.txt", "logged out"]
errors = ["failed login", "Error: File not found"]

# Generate 998 random log entries
for _ in range(998):
    user = random.choice(users)
    event = random.choice(events)
    timestamp = start_time + timedelta(minutes=random.randint(1, 10))
    log_entries.append(f"{timestamp} {user} {event}")
    start_time = timestamp

# Add 2 specific "failed login" entries
failed_logins = [
    f"{start_time + timedelta(minutes=5)} User6 failed login",
    f"{start_time + timedelta(minutes=10)} User8 failed login"
]
log_entries.extend(failed_logins)

# Write to sample_log.txt
with open('sample_log.txt', 'w') as file:
    for entry in log_entries:
        file.write(entry + '\n')
