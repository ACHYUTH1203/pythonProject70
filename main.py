import random
MAX_lines= 3
MAX_BET=100
MIN_BET=1
ROWS=3
COLS=3
symbol_count={
    "A":2,
    "B":4,
    "C":4,
    "D":6
}
symbol_value={
    "A":5,
    "B":4,
    "C":3,
    "D":2
}
def check_winnings(colums,lines,bet,values):
    winnings=0
    winnings_lines=[]
    for line in range(lines):
        symbol=colums[0][line]
        for column in colums:
            symbol_check=column[line]
            if symbol!=symbol_check:
                break
        else:
            winnings+=values[symbol]*bet
            winnings_lines.append(line+1)
    return winnings
def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range (symbol_count):
            all_symbols.append(symbol)
    columns=[]
    for _ in range(cols):
        column=[]
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns
def print_slot_mchine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i!=len(columns)-1:
                print(column[row],end=" | ")
            else:
                print(column[row],end="")
        print()
def deposit():
    while True:
        amount=input("WHAT WOULD YOU LIKE TO DEPOSIT? $ ")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("Enter an amount greater than zero")
        else:
            print("Please enter a number")
    return amount
def get_number_of_lines():
    while True:
        lines=input("ENTER NUMBER OF lines TO BET ON (1-"+str(MAX_lines)+")?")
        if lines.isdigit():
            lines=int(lines)
            if 1<=lines<=MAX_lines:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number")
    return lines
def get_bet():
    while True:
        amount=input("WHAT WOULD YOU LIKE TO BET ON EACH LINE $ ")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET<=amount<=MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET}-{MAX_BET}")
        else:
            print("Please enter a number")
    return amount
def spin(Balance):

    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        Total_bet = bet * lines
        if Total_bet > Balance:
            print(f"You dont have enough to bet yhat amount,your current balance is :${Balance}")
        else:
            break
    Total_bet = bet * lines
    print(f"You are betting ${bet} on {lines}.Total bet is equal to : ${Total_bet}")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_mchine(slots)
    winnings = check_winnings(slots, lines, bet, symbol_value)
    winnings_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", winnings_lines)
    return winnings-Total_bet

def main():
    Balance=deposit()
    while True:
        print(f"current balance is ${Balance}")
        answer=input("PRESS ENTER TO PLAY  (q TO QUIT)")
        if answer=="q":
            break
        Balance+=spin(Balance)
        print(f"You left with ${Balance}")

main()