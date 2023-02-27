#CAPSTONE PROJECT 
#For this task, assume that you have been approached by a small financial company and asked to create a program that allows the user to access two
#different financial calculators: an investment calculator and a home loan repayment calculator.
import math

print("\nChoose either 'investment' or 'bond' from the menu below to proceed:")
print("\ninvestment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")

#input for the type 

choice = input() # Take the input for the type “investment” or “bond” using the input() statement 

#CASE 1 INVESTMENT 
if  choice == 'investment' or choice == "INVESTMENT" or choice == 'Investment':
    #input for values
    deposit_amount = float(input("Enter deposit amount: ")) # we store the deposit amount in deposit_amount variable
    interest_rate = float(input("Enter the rate of interest: "))/100  # we store the interest rate in interest_rate variable and divided by 100
    number_years = int(input("Enter the number of years: ")) # we store the number of years in number_years variable
    type_interest = input("Enter the type of interest.\ncompound\nsimple\n") # we store the answer of the type of interest the user gives in type_interest

    #user selects the type of interest
    if type_interest == "simple": 
        total_amount = deposit_amount * (1 + interest_rate*number_years)  # we calculate the total amount as per formulae 
    elif type_interest == "compound":
        total_amount = deposit_amount * math.pow((1 + interest_rate), number_years) # we calculate the total amount as per formulae 
    else:
        print("Invalid type for interest selected!!!")
    print("The amount after", number_years, "years is", round(total_amount,2)) # we print out accordingly the result with 2 decimals only

# CASE2 Bond
elif choice == 'bond': # if the user enters bond we calculate accordingly 
    #input for values
    house_value = float(input("Enter the present value of the house: ")) # house value is stored in house_value
    interest_rate = float(input("Enter the rate of interest: "))/100/12 # we store the interest rate in interest_rate 
    num_months = int(input("Enter the number of months for the bond: ")) # we store the number of months in num_months
    repayment = (interest_rate * house_value)/(1 - (1 + interest_rate)**(-num_months)) # we calculate the repayment with the formulae
    print("The repayment after", num_months, "months is", round(repayment,2)) # we print out accordingly with 2 decimals only 

#INVALID CASE
else:
    print("Invalid choice!!")
    