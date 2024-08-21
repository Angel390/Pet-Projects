def calculate():
    try:
        # total = dist / mpg * ppg
        destination = input("Input destination/description: ")
        price_input = float(input("Input gas price price per gallon: "))    
        mpg_input = float(input("Input average miles per gallon: "))
        miles_input = float(input("Input distance traveled/will travel: "))

        total_price = miles_input / mpg_input * price_input
        total_price = round(total_price, 2)
        with open("gas.txt", "a") as file:
            file.write(f"{destination}|{total_price}\n")
        print(f"Total price: ${total_price:.2f}")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

def read_prices():
    with open("gas.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            destination, total_price = line.strip().split('|')
            print(f"Destination/description: {destination}")
            print(f"Cost: {total_price}")

def clear_gas_file():
    with open("gas.txt", "w") as file:
        pass

def display_menu():
    print("1 - Calculate gas prices")
    print("2 - Read destination/price log")
    print("3 - Clear the prices file")
    print("0 - Exit")

def main():
    actions = {
        1: calculate,
        2: read_prices,
        3: clear_gas_file,
    }

    while True:
        display_menu()
        try:
            mode = int(input("Please enter your choice: "))
            if mode in actions:
                actions[mode]()
            elif mode == 0:
                print("Shutting down")
                break
            else:
                print("Invalid Input!")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

if __name__ == "__main__":
    main()