# 🏦 Challenge #1 — ATM Cash Validator
# Your job: Write a Python program that:
# Asks the user to enter their account balance
# Asks how much they want to withdraw
# Checks these rules in order:
# Balance must be greater than 0
# Withdrawal amount must be greater than 0
# Withdrawal can't exceed balance
# ATM only dispenses multiples of 20 (e.g. 20, 40, 60… not 35)
# If all checks pass → print "✅ Dispensing $[amount]. New balance: $[remaining]"
# If any check fails → print a specific, helpful error message (not just "error")
def cash_validator():
        while True:
            try:
                current_balance = float(input("Enter your account balance: "))
                if current_balance <= 0:
                    print('Your balance must be greater than 0!')
                    continue
                while True:
                    amount_to_withdraw = float(input("Enter amount to withdraw. "
                                                     "(multiples of 20 e.g 20, 40, 60... " ))
                    if amount_to_withdraw <= 0:
                        print('Please enter correct number!')
                        continue
                    elif amount_to_withdraw > current_balance:
                        print('You do not have enough money!')
                        continue
                    elif amount_to_withdraw % 20 != 0:
                        print('ATM only dispenses multiples of 20 (e.g. 20, 40, 60… not 35)')
                        continue
                    else:
                        break
                remaining_balance = current_balance - amount_to_withdraw
                print(f'Dispensing {amount_to_withdraw}. New balance: {remaining_balance}')
                return
            except ValueError:
                print("Please enter a numeric value")
cash_validator()