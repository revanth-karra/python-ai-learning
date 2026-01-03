print("--- JARVIS SECURITY SYSTEM v1.0 ---")

# 1. Define correct credentials
sys_user = "Stark"
sys_pass = "Jarvis123"

# 2. Ask the user for input
username = input("Identify Yourself: ")
password = input("Enter Access Code: ")

# First, check if the username is correct
if username == sys_user:
    # if user is found, now check the password
    if password == sys_pass:
        print(f"Biometric scan complete. Welcome, Mr.{username}")
    else:
        print("ALERT: Identity confirmed, but Access Code is INCORRECT.")

else:
    print("UNKNOWN USER DETECTED. You're not Authorized!!!")

print("----------")