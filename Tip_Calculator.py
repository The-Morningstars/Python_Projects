print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

bill_per_person=(bill*(1+(tip/100))/people)

final_amount = round(bill_per_person, 3)
print(final_amount)

