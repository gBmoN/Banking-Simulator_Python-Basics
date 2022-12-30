
MENU = """
######################################################
|                                                    |
| Hey! Please select the option you wish to perform: |
|____________________________________________________|
|                                                    |
| d: Cash Deposit                                    |
| w: Withdraw Cash                                   |
| c: Consult Transactions                            |
| q: Quit                                            | 
|                                                    |
######################################################
"""

CASH_DEPOSIT ="""
######################################################
|___________________Cash Deposit_____________________|
|                                                    |
|        Enter the amount you want to deposit        |
|                                                    |
######################################################
"""

WITHDRAW_CASH ="""
######################################################
|___________________Withdraw Cash____________________|
|                                                    |
|        Enter the amount you want to withdraw       |
|                                                    |
######################################################
"""

CONSULT_TRANSACTIONS ="""
######################################################
|_________________Consult Transactions_______________|
|                                                    |
|                 Querying transactions              |
|                                                    |
######################################################
"""

error ="""
###########################################################################
|                                                                         |
| Invalid request, please enter one of the shortcuts provided in the menu |
|                                                                         |
###########################################################################
"""
import pandas as pd
from IPython.display import display

deposits = []
withdraws = []

while True:
    print(MENU)
    select = input()
    options = ['d', 'w', 'c', 'q']

    if select == 'q':
        break

    if select not in options:
        print("Invalid request")
        print("Please, enter a valid value")
        continue

    while True:
        balance = sum(deposits) - sum(withdraws)
        if select == 'd':
            print(CASH_DEPOSIT)

            while True:
                try:
                    deposit = float(input())
                    if deposit > 0:
                        break
                    else:
                        print("Invalid request")
                        print("Please, enter a valid value")
                        continue
                except ValueError:
                    print("Invalid request")
                    print("Please, enter a valid value")
            print(f"Are you sure you want to deposit ${deposit:.2f}?")
            confirm = input("""
                ...........
                | y - yes |
                | n - no  |
                |.........|
                """)
            if confirm == "y":
                print(f"OK! ${deposit:.2f} deposit done!")
                deposits.append(deposit)
                break
                

            elif confirm == "n":
                print("Do you want to deposit another amount?")
                confirm = input("""
                ...........
                | y - yes |
                | n - no  |
                |.........|
                """)
                if confirm == "y":
                    continue
                else: 
                    break
                
            else:
                print("Invalid request")
                print("Please, enter a valid value")
                continue
        elif select == 'w':
            print(WITHDRAW_CASH)
            
            while True:
                try:
                    withdraw = float(input())
                    if withdraw > 0 and withdraw <= balance:
                        break
                    else:
                        print("Insufficient funds")
                        print("Please, enter a valid value")
                        continue
                except ValueError:
                    print("Invalid request")
                    print("Please, enter a valid value")
            print(f"Are you sure you want to withdraw ${withdraw:.2f}?")
            confirm = input("""
                ...........
                | y - yes |
                | n - no  |
                |.........|
                """)
            if confirm == "y":
                print(f"OK! withdrawing ${withdraw:.2f}")
                withdraws.append(withdraw)
                break
                

            else:
                print("Do you want to withdraw another amount?")
                confirm = input("""
                ...........
                | y - yes |
                | n - no  |
                |.........|
                """)
                if confirm == "y":
                    continue
                else: 
                    break
                break
        
        elif select == 'c':
            print(CONSULT_TRANSACTIONS)
            balace = sum(deposits) - sum(withdraws)
            dict_deposits = {"Deposits":deposits}
            dict_withdraws = {"Withdraws":withdraws}
            print(f"Your balance is:{balace:.2f}")
            print("What do you want to view?")
            transaction = input("""
                 ................
                | d - Deposits   |
                | w - Withdraws  |
                |................|
                """)
            if transaction == 'd':
                transaction_deposits = pd.DataFrame(dict_deposits)
                display(transaction_deposits)
                break
            elif transaction == 'w':
                transaction_withdraws = pd.DataFrame(dict_withdraws)
                display(transaction_withdraws)
                break
            else:
                print("Invalid request")
                print("Please, enter a valid value")
                continue
        
