if __name__ == "__main__":
    fruits = ["apple", "banana","orange","pear","peach"]
    for i, value in enumerate(fruits, start=0):
        print(f'Index: {i}, Value: {value}')
    
    numbers = enumerate(fruits)
    for i in numbers:
        print(i)
