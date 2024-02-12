

def get_input(input_message, input_type):
    while(True):
        raw_input = input(f"{input_message}\n")
        try:
            user_input = input_type(raw_input)
            break
        except ValueError:
            print("Input is invalid")
    return user_input

while(True):
    nth_term = get_input("please give a number between 0 and 1000", int)
    fibonacci = [0, 1]
    if nth_term > 1000 or nth_term < 0:
        print("invalid range, please try again:")
    else:
        for x in range (0, nth_term - 1, 1):
            next_sequence = fibonacci[x] + fibonacci[x+1]
            fibonacci.append(next_sequence)
        print(fibonacci[nth_term])
    