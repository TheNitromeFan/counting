radixes = [1, 1]

def decimal_to_factorial(decimal_number):
    decimal_number = int(decimal_number)
    string = ""

    while radixes[-1] <= decimal_number:
        radixes.append(radixes[-1] * len(radixes))

    for radix in reversed(radixes):
        if radix <= decimal_number:
            string += str(decimal_number // radix) + ":"
            decimal_number = decimal_number % radix
        elif string != "":
            string += "0:"

    return string[:-3] + " | 0"


def factorial_to_decimal(factorial_number):
    if factorial_number[-4:] == " | 0":
        factorial_number = factorial_number[:-4]

    figits = [int(x) for x in factorial_number.split(":")]
    decimal_number = 0
    radix = 1

    for i, figit in enumerate(reversed(figits)):
        radix *= i + 1
        decimal_number += radix * figit

    return decimal_number


if __name__ == "__main__":
    print("Factorial/decimal base conversion program.\n"
          "Type a number to convert, 'switch' to switch modes,"
          " or nothing to quit.\n"
          "Entering decimal to factorial conversion mode...\n\n")
    modes = [decimal_to_factorial, factorial_to_decimal]
    mode = 0

    user_input = input("Enter number: ")
    while user_input != "":
        if user_input == "switch":
            if mode == 1:
                print("Switching to decimal to factorial conversion mode...\n")
                mode = 0
            else:
                print("Switching to factorial to decimal conversion mode...\n")
                mode = 1
        else:
            print(user_input, "=", modes[mode](user_input))

        user_input = input("Enter number: ")