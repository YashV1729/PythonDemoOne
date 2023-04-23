import random

MAX_LINE = 3
MAX_BET = 100
MIN_BET = 1


ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}



#Checking wins in slot 
def check_win(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][lines]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol]*bet
            winning_lines.append(line + 1)
            
    return winnings, winning_lines  


#Slot machine SPIN function
def get_slot_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] #used to copy the list not a reference
        for _ in range(rows): 
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns
    


#Function to Print the slot     
def get_slot_print(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns): 
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(columns[row], end="")
        print()
            
        
        
    

## Function for deposite 
def deposite():
    while True:
        amount = input("What would you like to deposite? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be grater than 0.")
        else:
            print("Please enter a number")
    return amount


## Function to get the number of lines to bet
def get_number_of_lines():
    while True:
        lines = input("Please enter the number of lines you want to bet on (1-" + str(MAX_LINE) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINE:
                break
            else:
                print("Lines must be greater than 0 ")
        else:
            print("Please enter a valid numbers of lines.")
    return lines


## Function to get amount user wants to bet on each line
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number")
    return amount


def game(balance):
    #balance= deposite
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
    
        if total_bet > balance:
            print(f"You have insufficient funds. Your Betting amount is: ${total_bet}")
        else:
            break
        
        
        print(f"You are betting ${bet} on {lines} lines. Total bet is ${total_bet} ")
        
    slots = get_slot_spin(ROWS, COLS, symbol_count)
    get_slot_print(slots)
    winnings, winning_lines = check_win(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    
    return winnings - total_bet


def main():
    balance = deposite()
    while True:
        print(f"Curent balance is ${balance}")
        answer = input("Press enter to play and q to quit. ")
        if answer == "q":
            break
        balance += game(balance)
    
    print(f"You left with ${balance} ")
    
main()