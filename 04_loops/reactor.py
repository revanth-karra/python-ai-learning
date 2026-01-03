# --- THE FOR LOOP (The Scanner) ---
core_stats = ["Normal", "Normal", "DANGER", "Normal", "DANGER"]

print("--- INITIATING SYSTEM SCAN ---")
# 'status' is a temporary variable that holds the current item
for status in core_stats:
    if status == "DANGER":
        print(f" ALERT: Reactor Core Unstable! Action Needed!!!")
    else:
        print(f"Core is Stable {status}")

print ("--- SCAN COMPLETE ---") 


# 1. The For Loop
systems = ["Navigation", "Engines", "Life Support", "Communications"]

print("--- PRE-FLIGHT CHECK ---")

for item in systems:
    print(f"Checking {item} ... OK")

print("All systems GO!\n")

#2. The While Loop
battery = 90

print("--- CHARGING STARTED ---")

# While the battery is not 100 yet ...
while battery < 100:
    print(f"Battery at {battery}% ... Charging ...")
    battery = battery + 2

print(f"Battery Full: {battery}%")
print("Ready for takeoff!")