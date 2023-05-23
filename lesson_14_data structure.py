# Task_1
A_june_debtors = set()
B_july_debtors = set()

june_input = input("Enter the names of the debtors for June (by whom): ")
A_june_debtors = set(june_input.split(","))

july_input = input("Enter the names of debtors for July (by whom): ")
B_july_debtors = set(july_input.split(","))

both_months_debtors = A_june_debtors.intersection(B_july_debtors)
print("Names of debtors for June and July:", both_months_debtors)

no_june_debt_debtors = B_july_debtors.difference(A_june_debtors)
print("Debtors for July without debt for June:", no_june_debt_debtors)

# Task_2
import re
strings = ["FirstItem", "FriendsList", "MyTuple"]

snake_case_strings = [re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower() for s in strings]
print("Рядки у форматі snake_case:", snake_case_strings)
