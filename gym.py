import random

def generate():
    days = ["Tuesday","Wednesday","Friday","Saturday"]
    group = ["Arms","Chest","Shoulders","Back"]
    random.shuffle(group)
    shuffled = [f"{day}: {grp}" for day, grp in zip(days, group)]
    shuffled.insert(2, "Thursday: Legs") 
    result = ", ".join(shuffled)
    with open("gym_schedule.txt", "a") as file:
        file.write(f"{result}\n")
    print(result)

def read_file():
    with open("gym_schedule.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line)

def clear_file():
    with open("gym_schedule", "w") as file:
        pass

def display_menu():
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
                print("Invalid input!")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

if __name__ == "__main__":
    main()