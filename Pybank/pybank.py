# Import the pathlib and csv
from pathlib import Path
import csv
#Set csv path
csvpath = Path("C://Users//Optiplex7040//Downloads//python-challenge-main1//Pybank/budget_data.csv")
#Initialize Variables
months = 0
total_losses = 0
changes_in_profit_losses = []
greatest_increase_month = ""
greatest_decrease_month = ""
greatest_profit_increase = 0
greatest_loss_profit = 0

#Read data from budget_data csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader, None)
    last_profit_loss = 0
    
    for row in csvreader:
        months += 1
        total_losses += int(row[1])
        lost_profit = int(row[1])

        change_in_profit_loss = lost_profit - last_profit_loss
        changes_in_profit_losses.append(change_in_profit_loss)
        
        if int(row[1]) > greatest_profit_increase:
            greatest_profit_increase = int(row[1])
            greatest_increase_month = row[0]
        if int(row[1]) < greatest_loss_profit:
            greatest_loss_profit = int(row[1])
            greatest_decrease_month = row[0]
            
            
        average_change = sum(changes_in_profit_losses) / (months)

#Print results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {months}")
print(f"Total: ${total_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_profit_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_loss_profit})")


#Set output file path 
output_file_path = 'pybank.txt'

#Open output path
with open(output_file_path, 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {months}\n")
    output_file.write(f"Total: ${total_losses}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_profit_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_loss_profit})\n")

print(f"Results exported to {output_file_path}")