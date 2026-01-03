from datetime import datetime, timedelta

# Dictionary to store festivals
festivals = {}

# Add a new festival
def add_festival():
    name = input("Enter festival name: ").strip()
    date_str = input("Enter festival date (YYYY-MM-DD): ").strip()

    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        festivals[name] = date
        print("✅ Festival added successfully!")
    except ValueError:
        print("❌ Invalid date format! Use YYYY-MM-DD")

# View all festivals
def view_festivals():
    if not festivals:
        print("⚠️ No festivals saved.")
        return

    print("\n📅 Saved Festivals:")
    for name, date in festivals.items():
        print(f"{name} → {date}")

# Delete a festival
def delete_festival():
    name = input("Enter festival name to delete: ").strip()
    if name in festivals:
        del festivals[name]
        print("🗑️ Festival deleted successfully!")
    else:
        print("❌ Festival not found.")

# Check reminders
def check_reminders():
    today = datetime.today().date()
    upcoming = today + timedelta(days=7)

    found = False
    for name, date in festivals.items():
        if date == today:
            print(f"🎉 Today is {name}!")
            found = True
        elif today < date <= upcoming:
            days_left = (date - today).days
            print(f"⏳ {name} is in {days_left} day(s)")
            found = True

    if not found:
        print("📭 No upcoming festivals.")

# Main menu
def main():
    while True:
        print("\n====== Festival Reminder Bot ======")
        print("1. View all festivals")
        print("2. Add new festival")
        print("3. Delete a festival")
        print("4. Check reminders")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            view_festivals()
        elif choice == "2":
            add_festival()
        elif choice == "3":
            delete_festival()
        elif choice == "4":
            check_reminders()
        elif choice == "5":
            print("👋 Exiting... Have a nice day!")
            break
        else:
            print("❌ Invalid choice! Try again.")

# Run program
if __name__ == "__main__":
    main()