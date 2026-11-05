import json
from datetime import datetime

file_name = "vehicles.json"


# Add Vehicle
def add_vehicle():
    try:
        with open(file_name, "r") as file:
            vehicles = json.load(file)
    except:
        vehicles = []

    print("\n--- Add Vehicle ---")

    name = input("Enter vehicle name: ")
    model = input("Enter vehicle model: ")
    number = input("Enter registration number: ")
    last_service = input("Enter last service date (DD-MM-YYYY): ")
    next_service = input("Enter next service date (DD-MM-YYYY): ")

    vehicle = {
        "name": name,
        "model": model,
        "number": number,
        "last_service": last_service,
        "next_service": next_service
    }

    vehicles.append(vehicle)

    with open(file_name, "w") as file:
        json.dump(vehicles, file, indent=4)

    print("\nVehicle added successfully!")


# View Vehicle History
def view_vehicles():
    try:
        with open(file_name, "r") as file:
            vehicles = json.load(file)
    except:
        vehicles = []

    if len(vehicles) == 0:
        print("\nNo vehicle history found.")
    else:
        print("\n--- Vehicle History ---")

        for vehicle in vehicles:
            print("\nVehicle:", vehicle["name"])
            print("Model:", vehicle["model"])
            print("Registration:", vehicle["number"])
            print("Last Service:", vehicle["last_service"])
            print("Next Service:", vehicle["next_service"])


# Service Reminder
def service_reminder():
    try:
        with open(file_name, "r") as file:
            vehicles = json.load(file)
    except:
        vehicles = []

    if len(vehicles) == 0:
        print("\nNo vehicles found.")
        return

    today = datetime.today().date()

    print("\n--- Service Reminders ---")

    for vehicle in vehicles:
        service_date = datetime.strptime(
            vehicle["next_service"], "%d-%m-%Y"
        ).date()

        days = (service_date - today).days

        print("\nVehicle:", vehicle["name"])

        if days > 0:
            print("Service due in", days, "days.")
        elif days == 0:
            print("Service is due today!")
        else:
            print("Service is overdue by", abs(days), "days.")


# Delete History
def delete_history():
    confirm = input("\nDo you want to delete all history? (yes/no): ")

    if confirm.lower() == "yes":
        with open(file_name, "w") as file:
            json.dump([], file)

        print("\nHistory deleted successfully!")
    else:
        print("\nDeletion cancelled.")


# Main Menu
while True:
    print("\n===== VEHICLE SERVICE REMINDER SYSTEM =====")
    print("1. Add Vehicle")
    print("2. View Vehicle History")
    print("3. Service Reminder")
    print("4. Delete History")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_vehicle()

    elif choice == "2":
        view_vehicles()

    elif choice == "3":
        service_reminder()

    elif choice == "4":
        delete_history()

    elif choice == "5":
        print("\nThank you for using the system!")
        break

    else:
        print("\nInvalid choice. Please try again.")
