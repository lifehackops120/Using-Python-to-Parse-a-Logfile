# Open the log file
with open('sample_log.txt', 'r') as file:
    # Read all lines in the file
    lines = file.readlines()

# Print lines that contain 'failed login'
failed_logins = 0
for line in lines:
    if 'failed login' in line:
        print(line.strip())
        failed_logins += 1

# Print the total number of failed logins
print(f"Total failed logins: {failed_logins}")
