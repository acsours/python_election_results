# import csv and read
import os
import csv

pybank_path = os.path.join('Resources','budget_data.csv')

csvfile = open(pybank_path)

csvreader = csv.reader(csvfile, delimiter=',')

# print(csvreader)
# read header row first
csv_header = next(csvreader)
print(f'CSV Header: {csv_header}')

# take data from two columns: date and profit/losses
# store date and profit/losses in containers
date = []
profit_losses = []

# iterate through each row
# and append to new lists


for row in csvreader:
    date.append(row[0])
    profit_losses.append(row[1])

# print(f'date is {date[0]} and profit/losses is {profit_losses[0]}')
# print(profit_losses[0])
print(f'{len(date)}{len(profit_losses)}')

# write to new file? where does this need to happen? before or after calculations? I think it happens after...- directions just say export text file with results
# calcluate:
    # total number of months in dataset (len)
    # net total amount of profit/losses over entire period
    # calculate changes in profit/losses over entire period, then find average of those changes
    # greatest increase in profits (date and amount) over entire period
    # greatest decrease in losses (date and amount) over entire period
'''
Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average  Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)
'''
# print analysis to terminal and export text file with results