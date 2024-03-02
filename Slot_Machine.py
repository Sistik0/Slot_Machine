import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

#dictionary that contains the symbols and their respective counts
SYMBOL_COUNT = {
    "Orange" : 6, 
    "Cherry" : 5,
    "Bell"   : 3, 
    "Bar"    : 2, 
    "7"      : 1
}

SYMBOL_VALUE = {
    "Orange" : 2, 
    "Cherry" : 2,
    "Bell"   : 3, 
    "Bar"    : 3, 
    "7"      : 6
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line+1)
    return winnings, winning_lines


def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, SYMBOL_COUNT in symbols.items():
        for _ in range(SYMBOL_COUNT):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

#transposing
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " | ")
            else:
                print(column[row], end = "")
        print()


#collects user input to obtain  deposit amount from the user
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines you would like to play (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Lines must be between 1 and " + str(MAX_LINES) + ".")
        else:
            print("Please enter a number.")

    return lines

def get_bet():
    while True:
        bet = input("Enter the amount you would like to bet on each line (1-" + str(MAX_BET) + ")? ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Bet must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return bet

def game(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough money to bet ${total_bet}. Your balance is ${balance}.")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, SYMBOL_COUNT)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, SYMBOL_VALUE)
    print(f"You won ${winnings}.")
    # * splat/unpack operator passes every single element of the list as a separate argument
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        if balance == 0:
            print("You have no money left. Game over.")
            break
        print(f"Current balance: ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += game(balance)

    print(f"You left with ${balance}")

main()