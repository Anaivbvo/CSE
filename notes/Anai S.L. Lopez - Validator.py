print("The Luhn Formula:")
number = input(">_")


def reverse_it(string):
    print(string[::-1])


def valid_card_number(num: str):
    # 1
    # Drop the last digit from the number. The last digit is what we want to check against
    print("1. Drop the last digit from the number. The last digit is what we want to check against:")
    new = number[:-1]
    print(new)
    print("-----")
    # 2
    # Reverse the numbers
    print("2. Reverse the numbers:")
    new2 = reverse_it(new)
    print("-----")
    # 3
    # Multiply the digits in odd positions (1, 3, 5, etc.) by 2 and subtract 9 to all any result higher than 9
    print("3. Multiply the digits in odd positions (1, 3, 5, etc.) by 2:")
    for index in range(len(number)):
        new2[index] = int(new2[index])
    print("-----")
    # 4
    # and subtract 9 to all any result higher than 9:
    print("4. and subtract 9 to all any result higher than 9:")
    print("-----")
    # 5
    # Add all the numbers together
    print("5. Add all the numbers together:")
    print("-----")
    # 6
    # The check digit (the last number of the card) is the amount that you would need to add to get a multiple of"
    # " 10 (Modulo 10
    print("6. The check digit (the last number of the card) is the amount that you would need to add to get a multiple "
          "of 10 (Modulo 10):")
    print("-----")


print(valid_card_number(number))
