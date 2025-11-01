# Given data
cost_of_meal = 44.50
restaurant_tax = 6.75 / 100 
tip = 15 / 100
tax_amount = cost_of_meal * restaurant_tax
total_with_tax = cost_of_meal + tax_amount
tip_amount = total_with_tax * tip
final_total = total_with_tax + tip_amount

# Display results
print(f"Cost of meal       : ${cost_of_meal:.2f}")
print(f"Restaurant tax (6.75%): ${tax_amount:.2f}")
print(f"Total with tax      : ${total_with_tax:.2f}")
print(f"Tip (15%)           : ${tip_amount:.2f}")
print(f"-------------------------------")
print(f"Final total to pay  : ${final_total:.2f}")
