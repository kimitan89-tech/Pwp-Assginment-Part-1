import os

# ==============================================================================
# HOUSEKEEPING MODULE
# ==============================================================================

def view_tasks():
    print("\n" + "="*40)
    print("      HOUSEKEEPING TO-DO LIST")
    print("="*40)
    print(f"{'Room ID':<10} | {'Status':<15}")
    print("-" * 30)

    try:
        # Open file in Read mode
        f = open("database/rooms.txt", "r")
        lines = f.readlines()
        f.close()

        count = 0 

        for line in lines:
            clean_line = line.strip()
            if len(clean_line) == 0: continue
            
            # Split line by comma to get columns: [ID, Type, Price, Status]
            data = clean_line.split(",") 

            if len(data) >= 4:
                room_id = data[0]
                status = data[3]

                # Filter to show only 'Dirty' or 'Maintenance' rooms
                if status == "Dirty" or status == "Maintenance":
                    print(f"{room_id:<10} | {status:<15}")
                    count = count + 1
        
        if count == 0:
            print("No active tasks. All rooms are clean.")

    except FileNotFoundError:
        print("Error: File 'database/rooms.txt' not found.")

def update_status():
    print("\n" + "="*40)
    print("      UPDATE ROOM STATUS")
    print("="*40)

    target_id = input("Enter Room ID to update: ")
    
    try:
        # Read all lines into memory first
        f = open("database/rooms.txt", "r")
        lines = f.readlines()
        f.close()

        found = False
        new_file_content = []

        for line in lines:
            clean_line = line.strip()
            if len(clean_line) == 0: continue

            data = clean_line.split(",")

            if len(data) < 4:
                new_file_content.append(line)
                continue

            current_id = data[0]
            current_status = data[3]

            # Check if this is the room we want to update
            if current_id == target_id:
                found = True
                print(f"Current Status: {current_status}")
                print("1. Available (Clean)\n2. Dirty\n3. Maintenance")
                choice = input("Select Status: ")

                if choice == "1": current_status = "Available"
                elif choice == "2": current_status = "Dirty"
                elif choice == "3": current_status = "Maintenance"
                
                print(f"Room {target_id} updated.")

            # Rebuild the line with the new status and add to list
            new_line = f"{data[0]},{data[1]},{data[2]},{current_status}\n"
            new_file_content.append(new_line)

        # Write the updated list back to the file
        if found:
            f = open("database/rooms.txt", "w")
            for line in new_file_content:
                f.write(line)
            f.close()
        else:
            print("Error: Room ID not found.")

    except FileNotFoundError:
        print("Error: File 'database/rooms.txt' not found.")

# ==============================================================================
# MAIN MENU
# ==============================================================================
def housekeeping_menu():
    while True:
        print("\n=== HOUSEKEEPING DASHBOARD ===")
        print("1. View Tasks")
        print("2. Update Room Status")
        print("3. Back")
        
        choice = input("Enter choice: ")
        
        if choice == '1': view_tasks()
        elif choice == '2': update_status()
        elif choice == '3': break
        else: print("Invalid input.")
