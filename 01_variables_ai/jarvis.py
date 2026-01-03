ai_name = "Jarvis"
ai_version = 1.0

print(f"Initializing {ai_name} system v{ai_version}...")
print("-----------------")

user_name = input("USER: Enter your identity: ")
user_role = input("USER: Enter your job role: ")
task_count = input("USER: How many tasks for today? ")

clean_name = user_name.strip().title()
clean_role = user_role.strip().upper()


num_tasks = int(task_count)
time_per_task = 2.5
total_time = num_tasks * time_per_task

print("\n[SYSTEM REPORT]")
print(f"User: {clean_name}")
print(f"Role: {clean_role}")
print(f"Workload: {num_tasks} tasks detected!!!")
print(f"Prediction: Estimated completion time is {total_time} minutes.")
print("System Standby.")