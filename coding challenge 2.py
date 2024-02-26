def credit_card(card_number):
    digits = list(card_number)  # Converting the card number to a list of characters to reverse it
    digits.reverse()  # Reverse the list of digits because the algorithm works from right to left
    total = 0 # giving total variable a value of zero for now

    for i in range(len(digits)):
        digit = digits[i]
        if i % 2 == 0: # if i is even it directly gets added to the total
            total += int(digit)
        else:
            doubled_digit = int(digit) * 2
            if doubled_digit > 9:# if number is higher than nine we have to add its digits
                total += (doubled_digit // 10) + (doubled_digit % 10)#//10 fortens palce and % 10 for ones place
            else:
                total += doubled_digit

    return total % 10 == 0 # if this comes true that means card is valid else it will show not valid

def card_type(card_number):
    if card_number.startswith('34') or card_number.startswith('37'):
        return 'This is a American Express'
    elif card_number.startswith(('51', '52', '53', '54', '55')):
        return ' This is a MasterCard'
    elif card_number.startswith('4'):
        return 'This is a Visa'
    else:
        return 'Unknown'

def user_input():
    card_number = input("Please enter your credit card number: ")
    if card_number.isdigit(): # makes sure that the entered input is numbers
        if credit_card(card_number):
            print(f"The credit card number {card_number} is a valid {card_type(card_number)} card.")
        else:
            print("Invalid credit card number.")
    else:
        print("Invalid input. Please enter a numeric value.")

user_input()



