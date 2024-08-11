import random

def random_numbers():
    size = int(input("Please enter the list size: "))
    start = int(input("Please enter the start number: "))
    stop = int(input("Please enter the stop number: "))

    numbers = [0 for _ in range(size)]
    i = 0
    while i < size:
        numbers[i] = random.randint(start,stop)
        i += 1
    print(*numbers, sep = ", ")
    
    with open("lists.txt", "a") as file:
        file.write(f"{numbers}\n,")

def unique_random_numbers():
    size = int(input("Please enter the list size: "))
    start = int(input("Please enter the start number: "))
    stop = int(input("Please enter the stop number: "))

    number_set = set()
    if (stop - start) > size:
        while len(number_set) < size:
            number_set.add(random.randint(start,stop))
    print(*number_set, sep = ", ")

    with open("lists.txt", "a") as file:
        file.write(f"{number_set}\n,")

def clear_file():
    with open("lists.txt", "w") as file:
        pass

def display_menu():
    print("Options:")
    print("1 - Generate random numbers")
    print("2 - Generate unique random numbers")
    print("3 - Clear the lists file")
    print("0 - Exit")

def main():
    actions = {
        1: random_numbers,
        2: unique_random_numbers,
        3: clear_file,
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