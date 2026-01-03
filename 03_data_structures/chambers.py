#1. Create a list of Iron Man Suits
suits = ["Mark I", "Mark II", "Mark III", "Mark IV"]

print("--- STARK INDUSTRIES INVENTORY---")

#2. print the entire list
print(f"Current Suits: {suits}")

#3. Access a specific item (Remember: Computers count from 0)
first_suit = suits[0]
print(f"Original Prototype: {first_suit}")

#4. Access the last item, python trick -1 means last one remember ;)
last_suit = suits[-1]
print(f"Last model: {last_suit}")

#5. Add a new item to the list
suits.append("Tony")
print(f"New Inventory {suits}")


print("\n---- SYSTEM DIAGNOSTICS ----")

#1. Create a Dictionary (Key: Suite name, Value: Power Level)

suit_power = {"Mark I": 15, "Mark II": 50, "Mark III": 85, "Mark IV": 90}

current_level = suit_power["Mark I"]
print(f"Mark I Power Level is:{current_level}")

suit_power["Stark"] = 500
print(f"Added Stark. Power: {suit_power["Stark"]}")

query = input("Enter which suit do you want to check? ")
print(f"Checking database for {query}")
print(f"Status: {suit_power[query]}%")


print("\n--- COMBINED HYBRID DATA ---")

# A LIST OF DICTIONARIES
inventory = [{"name": "Mark I", "energy": 15, "status": "Decommissioned"}, {"name": "Mark II", "energy": 90, "status": "Active"}, {"name": "Hulk", "energy": 500, "status": "Standby"}]

# Accessing complex data
selected_suit = inventory[1]
print(f"Selected Suit: {selected_suit['name']}")
print(f"Status Report: {selected_suit["status"]}")

print(f"Full Database: {inventory}")