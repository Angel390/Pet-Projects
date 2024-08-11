import matplotlib.pyplot as plt

def main():
    input = 1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,0,0,0,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1
    
    success_total = 0
    fail_total = 0
    
    success = 0
    fail = 0

    success_array = []
    fail_array = []
    
    for value in input:
        if value == 0:
            fail_total += 1
        elif value == 1:
            success_total += 1

    for value in input:
        if value == 1:
            success += 1
        elif value == 0:
            if success != 0:
                success_array.append(success)
                success = 0
    if success != 0:
        success_array.append(success) # Account for the last segment
    
    for value in input:
        if value == 0:
            fail += 1
        elif value == 1:
            if fail != 0:
                fail_array.append(fail)
                fail = 0
    if fail != 0:
        fail_array.append(fail) # Account for the last segment

    success_rate = round((success_total / (fail_total + success_total)),2)

    print(*success_array, sep = ", ")
    print(*fail_array, sep = ", ")
    print(success_rate)

    x_success = list(range(1, len(success_array) + 1))
    x_fail = list(range(1, len(fail_array) + 1))
    plt.bar(x_success, success_array, color = 'g', label = 'Successes')
    plt.bar(x_fail, fail_array, color = 'r', label = "Failures")
    plt.xlabel('Segment Number')
    plt.ylabel('Length of Segment')
    plt.title('Frequency of Sucesses and Failures')
    plt.legend()
    plt.show()

main()