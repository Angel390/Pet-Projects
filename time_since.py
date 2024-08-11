import datetime

def create_event():
    date_input = input("Input event start date and time (YYYY-MM-DD HH:MM:SS) or press Enter for current time: ")
    if date_input:
        try:
            event_start = datetime.datetime.strptime(date_input, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            print("Invalid format! Using current time instead.")
            event_start = datetime.datetime.now()
    else:
        event_start = datetime.datetime.now()
    event = input("Input event: ")
    with open("events.txt", "a") as file:
        file.write(f"{event}|{event_start.isoformat()}\n")

def read_event():
    event_end = datetime.datetime.now()
    with open("events.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            event, event_start_str = line.strip().split('|')
            event_start = datetime.datetime.fromisoformat(event_start_str)
            event_duration = event_end - event_start
            print(f"Event: {event}")
            print(f"Event Start: {event_start}")
            print(f"Duration: {event_duration}")

def clear_event_file():
    with open("events.txt", "w") as file:
        pass

def display_menu():
    print("Options:")
    print("1 - Create an event")
    print("2 - Check the duration of an event")
    print("3 - Clear the event file")
    print("0 - Exit")

def main():
    actions = {
        1: create_event,
        2: read_event,
        3: clear_event_file
    }
    while True:
        display_menu()
        try:
            mode = int(input("Please enter your choice: "))
            if mode in actions:
                actions[mode]()
            elif mode == 0:
                print("Exiting the program.")
                break
            else:
                print("Invalid input!")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
if __name__ == "__main__":
    main()