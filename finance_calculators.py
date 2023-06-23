import math

#this program allows a user to calculate interest on an investment, or repayments needed on a home loan

#user choses an option from the two choices below

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

#additional questions will be presented depending on the option selected

if user_choice == 'investment' or user_choice == 'Investment' or user_choice == 'INVESTMENT':
    print("Thank you,")
    investment_amount = (float(input("Please specify the amount you are depositing: ")))
    investment_interest_rate = (float(input("Please specify your interest rate (number only): ")))
    investment_years = (int(input("Please specify the number of years you plan on investing for: ")))
    interest = (input("Please enter either 'simple' or 'compound' depending on the type of interest that applies to you: "))
    
#if investment is selected, interest will be calculated on the investment amound depending on whether the user selects 'simple' or 'compound'

    if interest == 'simple' or interest == 'Simple' or interest == 'SIMPLE':
        print("Your total amount after simple interest has been applied is: ")
        print(investment_amount * (1 + (investment_interest_rate / 100) * investment_years))

    elif interest == 'compound' or interest == 'Compound' or interest == 'COMPOUND':
        print("Your total amound after compound interest has been applied is: ")
        print(investment_amount * math.pow((1 + (investment_interest_rate / 100)) , investment_years))
        
#if bond is selected, monthly repayment amount will be calculated depending on user responses to the below queries

elif user_choice == 'bond' or user_choice == 'Bond' or user_choice == 'BOND': 
    print("Thank you")
    property_value = (float(input("Please specify the value of your property: ")))
    property_interest_rate = (float(input("Please specify your interest rate (number only): ")))
    repayment_time = (int(input("Please specify the number of months you plan to take to repay the bond: ")))

    property_monthy_interest = ((property_interest_rate / 100) / 12)
   
    print("The total amount you will need to repay on this bond each month is: ")
    print((property_monthy_interest * property_value) / (1 - (1 + property_monthy_interest) ** (-repayment_time)))

else:
    print("Invalid option, please specify bond, or investment")


    

