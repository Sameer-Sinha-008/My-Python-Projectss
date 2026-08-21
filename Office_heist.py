import random
# Player States
moves_left = 10
inventory = []
current_room = "My Cubicle"
boss_room = "server room"
all_rooms = ["Corridor", "Break Room", "Server Room"]
# World Data (Office Heist)
rooms = {
    "My Cubicle": {
        "description": "Aap apne cubicle par ho. Boss break par gaya hai, aapke paas 10 moves hain!",
        "corridor": "Corridor"
    },
    "Corridor": {
        "description": "Office ka main corridor. Yahan se Break Room aur Server Room ke raste hain.",
        "server": "Server Room",
        "break_room": "Break Room",
        "back": "My Cubicle"
    },
    "Break Room": {
        "description": "Break room mein table par ek Access Card rakha hua mila!",
        "item": "Access Card",
        "back": "Corridor"
    },
    "Server Room": {
        "description": "Server Room ka terminal! Yahan aapki bad appraisal sheet rakhi hai.",
        "back": "Corridor"
    }
}

print("=== 🏢 THE OFFICE HEIST 🏢 ===")
print("Boss ke aane se pehle file delete karo!\n")

while moves_left > 0:
    # 1. Win Check
    if current_room == "Server Room" and "Access Card" in inventory:
        print("\nCONGRATULATIONS!! You Deleted the File!")
        print("YOU WON THE GAME!!")
        break

    # 2. Boss Check
    if current_room == boss_room:
        print("\n🚨 Boss CAUGHT You!! GAME OVER!")
        break

    # 3. Print Room Details
    print(f"\nLocation: {current_room}")
    print(f"Moves_Left: {moves_left}")
    print(f"Inventory: {inventory}")
    print(rooms[current_room]["description"])

    # 4. Action Input
    action = input("What You Wanna Do? (Go/Take) ").strip().lower()

    # 5. Room Navigation & Locked Door
    if action in rooms[current_room]:
        next_room = rooms[current_room][action]
        if next_room == "Server Room" and "Access Card" not in inventory:
            print("\n🔒 Access Denied! First Get The Access Card")
        else:
            current_room = next_room
            moves_left -= 1
            boss_room = random.choice(all_rooms)

    # 6. Take Item
    elif action == "take" and "item" in rooms[current_room]:
        item_name = rooms[current_room]["item"]
        inventory.append(item_name)
        print(f"You picked {item_name}")
        del rooms[current_room]["item"]
        moves_left -= 1

    else:
        print("Command is WRONG!!")

# Loop ke bilkul baahar
if moves_left == 0:
    print("\nMoves End! Game Over!")
