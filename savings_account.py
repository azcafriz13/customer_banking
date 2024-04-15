#Import the Account class from the Account.py file
from Account import Account
# Define a function for the Savings Account.
def create_savings_account(balance, interest_rate, months):
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    savings_account = Account(balance,0)    
    # Calculate interest earned
    interest = balance * (interest_rate / 100 * months / 12)
    # Update the savings account balance by adding the interest earned
    balance += interest
    # Pass the updated_balance to the set balance method using the instance of 
    # the SavingsAccount class.
    savings_account.set_balance(balance)
    # Pass the interest_earned to the set interest method using the instance of 
    # the SavingsAccount class.
    savings_account.set_interest(interest)
    # Return the updated balance and interest earned.
    return balance, interest

   

