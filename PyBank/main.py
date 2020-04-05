import csv
import os

file = "Resources/budget_data.csv"

output_path = os.path.join("financial_analysis.txt")

month_count = 0
pl_nettotal = 0
month_1 = 0
pl_changes = []
previous_month = 0
greatest_increase = ["",0]
greatest_decrease = ["",99999999999]



with open(file, 'r') as f:
    reader = csv.DictReader(f, delimiter=",")
    for row in reader:
        month_count += 1
        pl_nettotal += int(row["Profit/Losses"])
        month_1 = int(row["Profit/Losses"])
        if previous_month != 0: 
            pl_changes.append(month_1 - previous_month)
        change = month_1 - previous_month
        if change > greatest_increase[1]:
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = change
        if change < greatest_decrease[1]:
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = change
        previous_month = month_1
avg_change = round(sum(pl_changes)/len(pl_changes),2)

print("Financial Analysis")
print("------------------------------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${pl_nettotal}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
        
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=' ')
    csvwriter.writerows([["Financial", "Analysis"],
         "-" *20,
        ["Total", "Months:", month_count],
        ["Total:", "$", pl_nettotal],
        ["Average", "Change:", "$", avg_change],
        ["Greatest", "Increase", "in", "Profits:", greatest_increase[0], "$", greatest_increase[1]],
        ["Greatest", "Decrease", "in", "Profits:", greatest_decrease[0], "$", greatest_decrease[1]]
    ])



