import random

def generate():
    days = ["Day 1","Day 2","Day 3","Day 4"]
    group = ["Arms","Chest","Shoulders","Back"]
    random.shuffle(group)
    shuffled = [f"{day}: {grp}" for day, grp in zip(days, group)]
    result = ", ".join(shuffled)
    with open("gym_schedule.txt", "a") as file:
        file.write(f"{result}\n")
    print(result)

def read_file():
    try:
        with open("gym_schedule.txt", "r") as file:
            lines = file.readlines()
            if len(lines) == 0:
                print("The file is empty")
                return
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print("The file does not exist. Please generate a schedule first")

def clear_file():
    with open("gym_schedule.txt", "w") as file:
        pass

def display_menu():
    print("Legs are combined with other muscle groups")
    print("Options:")
    print("1 - Generate schedule")
    print("2 - Read the schedule file")
    print("3 - Clear the schedule file")
    print("0 - Exit")

def main():
    actions = {
        1: generate,
        2: read_file,
        3: clear_file,
    }
    while True:
        display_menu()
        try:
            mode = int(input("Please enter your choice: "))
            if mode in actions:
                actions[mode]()
            elif mode == 0:
                print("Exiting the generator.")
                break
            else:
                print("Invalid option. Please choose from 0 to 3")
        except ValueError:
            print("Invalid input! Please enter a numeric value between 0 and 3.")

if __name__ == "__main__":
    main()