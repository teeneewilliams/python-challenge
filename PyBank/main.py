import os
import csv

# establish the path to reference data and read in csv data
csvpath = os.path.join ("resources", "budget_data.csv")

# Store the contents of the variables into lists
month_list = []
revenue_changes = []

# open and read csv; csv reader specifies delimiter and variable that holds contents
with open(csvpath,"r") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)

# Loop through all the rows of data after the header and rename header
    for row in csv_reader:
        month_list.append(str(row[0]))
        revenue_changes.append(int(row[1]))

# # Calculate the totals to print datalines
total_months = len(month_list)

# calculate the net profit/loss
net_profit_loss = 0

for x in revenue_changes:
    net_profit_loss = net_profit_loss + x

# what is the average profit/loss - reset list then set to 0
average_monthly_change_list = []
previous_month_amount = 0

for x in range(len(revenue_changes)):
    if x == 0:
        previous_month_amount = revenue_changes[x]
    else:
        monthly_change = revenue_changes[x] - previous_month_amount
        average_monthly_change_list.append(monthly_change)
        previous_month_amount = revenue_changes[x]

# track monthly change

length = len(average_monthly_change_list)
total = sum(average_monthly_change_list)
profit_loss_average = (round(total / length,2))
print(profit_loss_average)

# declare variables for min and max profit/loss and matching month
month_greatest_increase = ''
amount_greatest_increase = 0
month_greatest_decrease = ''
amount_greatest_decrease = 0

for x in range(len(average_monthly_change_list)):
    if average_monthly_change_list[x] > amount_greatest_increase:
        amount_greatest_increase = average_monthly_change_list[x]
        month_greatest_increase = month_list[x+1]
    elif average_monthly_change_list[x] < amount_greatest_decrease:
        amount_greatest_decrease = average_monthly_change_list[x]
        month_greatest_decrease = month_list[x+1]

# print output
print("------------------------")
print("Profits and Losses Report")
print("------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${net_profit_loss}')
print(f'Average Change: ${profit_loss_average}')
print(f'Greatest Increase in Profits: {month_greatest_increase} for ${amount_greatest_increase}')
print(f'Greatest Decrease in Profits: {month_greatest_decrease} for ${amount_greatest_decrease}')

# output to text file
output_file = os.path.join("resources", "budget_data.txt")
with open(output_file, "w") as text_file:
    
    # store all of the text inside a variable called lines
    # writer = text_file.writer()
    # print(text_file.writer)

    # initialize text_file.writer
    text_file.write("------------------------\n")
    text_file.write("Profits and Losses Report\n")
    text_file.write("------------------------\n")
    text_file.write(f"Total Months: {total_months}\n")
    text_file.write(f"Total: ${net_profit_loss}\n")
    text_file.write(f"Average Change: ${profit_loss_average}\n")
    text_file.write(f"Greatest Increase in Profits: {month_greatest_increase} for ${amount_greatest_increase}\n")
    text_file.write(f"Greatest Decrease in Profits: {month_greatest_decrease} for ${amount_greatest_decrease}\n")