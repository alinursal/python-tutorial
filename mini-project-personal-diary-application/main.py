import os
from datetime import datetime

def create_entry(file_name, entry, add_timestamp=False):
    try:
        with open(file_name, 'a') as file:
            if add_timestamp:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"{timestamp} - {entry}\n")
            else:
                file.write(f"{entry}\n")
        print("Diary entry added successfully.")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")

def view_entries(file_name):
    try:
        if not os.path.exists(file_name):
            raise FileNotFoundError(f"The diary file '{file_name}' does not exist.")
        
        with open(file_name, 'r') as file:
            entries = file.readlines()
            if not entries:
                print("No diary entries found.")
            else:
                print("Diary Entries:")
                for entry in entries:
                    print(entry.strip())
    except FileNotFoundError as e:
        print(e)
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")

def main():
    file_name = "diary.txt"
    
    while True:
        print("\nDiary Menu:")
        print("1. Create a new diary entry")
        print("2. View previous diary entries")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            entry = input("Enter your diary entry: ")
            timestamp_option = input("Do you want to add a timestamp? (y/n): ").lower()
            add_timestamp = timestamp_option == 'y'
            create_entry(file_name, entry, add_timestamp)
        
        elif choice == '2':
            view_entries(file_name)
        
        elif choice == '3':
            print("Exiting the diary application.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()