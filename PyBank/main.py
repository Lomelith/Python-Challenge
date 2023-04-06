# I put comments in the other program first then got lazy
# so enjoy this otherwise comment free code
# I'm sure you will figure it out
# Also this data matches what i got from bootcamp spot, but not the screenshots.

import os
import csv

currentDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(currentDir)

resourcePath = os.path.join("Resources", "budget_data.csv")
analysisPath = os.path.join("Analysis", "analysis.txt")
total = 0
months = 0
greatestIncrease = 0
greatestDecrease = 0
profit = 0

with open(resourcePath, "r") as budget_data:
    budget_data = csv.DictReader(budget_data)

    for row in budget_data:
        temp = profit
        profit = int(row["Profit/Losses"])

        if profit > greatestIncrease:
            greatestIncrease = profit
            increaseStr = row["Date"] + " ($" + row["Profit/Losses"] + ")"
        if profit < greatestDecrease:
            greatestDecrease = profit
            decreaseStr = row["Date"] + " ($" + row["Profit/Losses"] + ")"

        change = profit - temp
        averageChange = change + change
        months += 1
        total += int(row["Profit/Losses"])

averageChange = averageChange / months

with open(analysisPath, "w") as analysis:
    print (f"Financial Analysis \n{'-'*30}\nTotal Months: {months}", file = analysis)
    print (f"Total: ${total}", file = analysis)
    print (f"Average Change: ${'{:.2f}'.format(averageChange)}", file = analysis)
    print (f"Greatest Increase in Profits: {(increaseStr)}", file = analysis)
    print (f"Greatest Decrease in Profits: {(decreaseStr)}", file = analysis)

print (f"\nFinancial Analysis \n{'-'*30}\nTotal Months: {months}")
print (f"Total: ${total}")
print (f"Average Change: ${'{:.2f}'.format(averageChange)}")
print (f"Greatest Increase in Profits: {(increaseStr)}")
print (f"Greatest Decrease in Profits: {(decreaseStr)}\n")