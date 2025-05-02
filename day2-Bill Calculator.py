print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people=int(input("How many people to split thge bill? "))
tip_as_percent = tip_percentage / 100
total_tip = total_bill * tip_as_percent
total_bill_with_tip = total_bill + total_tip
bill_per_person = total_bill_with_tip / people
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")
# 1. Welcome the user to the tip calculator.
# 2. Ask for the total bill amount.
# 3. Ask for the percentage tip you want to give.
# 4. Calculate the tip amount.
# 5. Calculate the total bill amount (bill + tip).
# 6. Ask how many people to split the bill.
# 7. Calculate the amount each person should pay.
# 8. Format the result to 2 decimal places.
# 9. Print the final amount each person should pay.
# 10. End the program.