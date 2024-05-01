# Import the pathlib and csv
from pathlib import Path
import csv
#Set csv path
csvpath = Path("C://Users//Optiplex7040//Downloads//python-challenge-main1//Pybank/budget_data.csv")

#Initialize Variables# Initialize variables
total_months = 0
net_total = 0
previous_profit_loss = 0
changes_list = []
greatest_increase = {"date": "", "amount": float("-inf")}
greatest_decrease = {"date": "", "amount": float("inf")}

# Open the CSV file
with open(csvpath, 'r') as csvfile:
    # Create a CSV reader object
    csvreader = csv.reader(csvfile)

    # Skip the header row
    header = next(csvreader)

    # Iterate through each row in the CSV file
    for row in csvreader:
        # Extract date and profit_loss from the current row
        date = row[0]
        profit_loss = int(row[1])

        # Update variables
        total_months += 1
        net_total += profit_loss

        # Calculate the change in profit/loss from the previous month
        if total_months > 1:
            change = profit_loss - previous_profit_loss
            changes_list.append(change)

            # Update greatest increase and decrease
            if change > greatest_increase["amount"]:
                greatest_increase["date"] = date
                greatest_increase["amount"] = change
            elif change < greatest_decrease["amount"]:
                greatest_decrease["date"] = date
                greatest_decrease["amount"] = change

        # Update previous_profit_loss for the next iteration
        previous_profit_loss = profit_loss

# Calculate the average change
average_change = sum(changes_list) / len(changes_list)

# Print the results
print("Financial Analysis")
print("_____________________________")
print(f"Total Months: {total_months}")
print(f"Net Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Losses: {greatest_decrease['date']} (${greatest_decrease['amount']})")
