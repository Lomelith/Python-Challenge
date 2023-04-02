import os
import csv

resourcePath = os.path.join("PyBank", "Resources", "budget_data.csv")
analysisPath = os.path.join("PyBank", "Analysis", "analysis.txt")
total = 0
months = 0
greatestIncrease = 0
greatestDecrease = 0
profit = 0
change = 0

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
        months +=1
        total += int(row["Profit/Losses"])

averageChange = averageChange / months

with open(analysisPath, "w") as analysis:
    analysis.write ("Financial Analysis \n--------------------------\nTotal Months: ")
    analysis.write (str((months)))
    analysis.write ("\nTotal: $")
    analysis.write (str((total)))
    analysis.write ("\nAverage Change:: $")
    analysis.write (str('{:.2f}'.format(averageChange)))
    analysis.write ("\nGreatest Increase in Progits: ")
    analysis.write (str((increaseStr)))
    analysis.write ("\nGreatest Decrease in Progits: ")
    analysis.write (str((decreaseStr)))

print (months)
print (total)
print ('{:.2f}'.format(averageChange))
print (increaseStr)
print (decreaseStr)