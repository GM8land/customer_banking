# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():

    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input("Enter the savings balance: "))
    savings_interest = float(input("Enter the interest rate: "))
    savings_months = int(input("Enter the number of months to calculate: "))

    # # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_months)

    # # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # print(f"${interest_earned: ,.2f} {updated_savings_balance: ,.2f}")
    print(f"Savings Interest Earned: ${interest_earned:,.2f} | Updated Balance in Savings: ${updated_savings_balance:,.2f}")
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input("Enter the CD Balance:  "))
    cd_interest = float(input("Enter the interest rate:  "))
    cd_months = int(input("Enter the number of months to calculate:  "))
    # # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_months)

    # # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # print(f"${interest_earned: ,.2f} {updated_cd_balance: ,.2f}")

    print(f"CD Interest Earned: ${interest_earned:,.2f} | Updated Balance in CD: ${updated_cd_balance:,.2f}")

 
    # Call the main function.
if __name__ == "__main__":
    main()