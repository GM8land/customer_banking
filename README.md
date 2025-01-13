## Module 3 Challenge: Customer Banking

### Challenge Instructions

You'll be creating a customer banking system that allows users to calculate and track interest earned on savings and CD accounts. By running this application, users will be able to enter their savings and CD account information, see the interest earned, and view the updated balances after a specified number of months.
The starter files consist of the following files: Accounts.py, savings_account.py, cd_account.py, and customer_banking.py. The Accounts.py file contains the Account class with methods to set the balance and interest.

In the savings_account.py file, you will import the Account class and create a create_savings_account function that will create a savings account instance, calculate the interest earned based on user input, update the account balance with the earned interest, and return the updated balance and interest earned.

In the cd_account.py file, you will import the Account class and create a create_cd_account function that will create a CD account instance, calculate the interest earned based on user input, update the account balance with the earned interest, and return the updated balance and interest earned.

In the customer_banking.py file, you will import the create_savings_account and create_cd_account functions, then create a main function that prompts the user to enter the savings and CD account details, call the corresponding functions to calculate the interest earned and update the balances, and display the results.

### Requirements

- Create the Savings Account Function (35 points)
  - The Account class from the Accounts.py file is imported. (4 points)

  - In the create_savings_account function, an instance of the Account class is created and the 
  balance and interest parameters are passed to the Account class. (6 points)

  - The interest earned is calculated and assigned to a variable. (4 points)

  - The savings account balance is updated by adding the interest earned to the balance and 
  assigned to a variable. (4 points)

  - The updated balance is passed to the set balance method using the instance of the Account 
  class. (6 points)

  - The interest earned is passed to the set balance method using the instance of the Account 
  class. (6 points)

  - The updated balance and interest earned are returned by the function. (5 points)

- Create the CD Account Function (35 points)
  - The Account class from the Accounts.py file is imported. (4 points)

  - In the create_cd_account function, an instance of the Account class is created and the   
    balance and interest parameters are passed to the Account class. (6 points)

  - The interest earned is calculated and assigned to a variable. (4 points)

  - The CD account balance is updated by adding the interest earned to the balance and assigned     to a variable. (4 points)

  - The updated balance is passed to the set balance method using the instance of the Account 
  class. (6 points)

  - The interest earned is passed to the set balance method using the instance of the Account 
  class. (6 points)

  - The updated balance and interest earned are returned by the function. (5 points)

- Create the Main Function (30 points)
  - The user is prompted to set the savings balance, interest rate, and months for the savings 
  account. (8 points)

  - Code is written to print out the interest earned and updated savings account balance with 
  interest earned for the given months. The values are formatted to two decimal places and  
  thousandths. (6 points)

  - The user is prompted to set the savings balance, interest rate, and months for the CD account. 
  (8 points)

  - Code is written to print out the interest earned and updated CD account balance with interest 
  earned for the given months. The values are formatted to two decimal places and thousandths. (6 
  points)

  - The main function is called to run the program. (2 points)

### Grade: 95
### Feedback from Grader
The provided code demonstrates a solid understanding of class creation and method implementation in Python, as well as using these methods to perform specific tasks such as creating CD and savings accounts, calculating interest, and updating balances. 



The `Account` class is well-defined with appropriate methods for setting balance and interest. The functions `create_cd_account` and `create_savings_account` correctly instantiate the `Account` class, calculate interest, and update the balance using the class methods. The main function effectively prompts the user for inputs, calls the relevant functions, and displays the results. However, there are a few minor issues, such as the redundant addition of interest to the updated balance and minor inconsistencies in variable naming (e.g., `interest` should be `interest_rate` in the function arguments for clarity). 



Additionally, the placement of import statements should be standardized, and the function definitions should be placed before the main execution block for better readability and structure. Overall, the code is functional and well-structured, demonstrating good practices in class usage and user interaction. Great job Geoff!
Central Grader , May 26, 2024 at 8:38am
