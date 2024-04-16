print("Welcome to the tip calculator!")

tt_bill = float(input("What was the total bill? $"))
tip_percent = int(input(f"What percentage tip would you like to give? 10, 12 or 15? "))
total_people = int(input("How many people to split the bill? "))

percent = tt_bill * tip_percent / 100

final_bill = (tt_bill + percent) / total_people
finalfinal_bill = "{:.2f}".format(final_bill) 
print(f"each person should pay: ${finalfinal_bill}")
