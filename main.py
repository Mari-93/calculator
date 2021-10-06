#############
# This script is created for calculator operations
# Author:
# Created at:
# Last modified at:
###############


import calculator as calc


print('Choose the choice')
for k, v in calc.calc_operation.items():
    print(k, v.__name__)

while True:
    n = int(input("Enter a choice: "))

    if calc.calc_operation.get(n):
        result = calc.calc_operation.get(n)()

        print(result)
    else:
        print("choose only from the option")
