import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")
found = False

# Open the CSV
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #Read the header row first
    header = next(csvreader)

    #Set variables as lists
    months = []
    profit_loses = []

    #loop to add all of the data of each row and colum into one single list
    for profit in csvreader:
        months.append(profit[0]) #set the row 0 as months
        profit_loses.append(float(profit[1])) #set the row 1 as profit loses

    months_count = len(months)
    #print(months_count)

    profit_count = sum(profit_loses)
    #print(profit_count)

    #change in the profit loses
    change_profit = []
    for i in range(len(profit_loses) - 1):
        f = profit_loses[i + 1] - profit_loses[i]
        change_profit.append(f)

    #average change in profit_loses
    average_change = (sum(change_profit) / len(change_profit))
    #print(average_change)

    # greatest increase in profit_loses
    max_profit = max(change_profit)

    # Find the month for Greatest Increase in Profits
    max_month_profit = months[change_profit.index(max_profit)+1]

    # Find Greatest Decrease in Profits
    min_profit = min(change_profit)

    # Find the mont Greatest Decrease in Profits
    min_month_profit = months[change_profit.index(min_profit)+1]

    # Print the analysis to the terminal
    print("Financial Analysis")
    print("-" * 20)
    print("Total months: {0}".format(str(months_count)))
    print("Total: ${0}".format(str(round(profit_count))))
    print("Average change: ${0}".format(str(round(average_change,2))))
    print("Greatest Increase in Profits: {0} (${1})".format(max_month_profit,str(round(max_profit))))
    print("Greatest Decrease in Profits: {0} (${1})".format(min_month_profit,str(round(min_profit))))

#Open or if file does not exist then create file named resutlpybank.txt
with open("ResultPyBank.txt", "w") as result:
    result.write("Financial Analysis" + "\n")
    result.write("-" * 20 + "\n")
    result.write("Total months: {0}".format(str(months_count)) + "\n")
    result.write("Total: ${0}".format(str(round(profit_count))) + "\n")
    result.write("Average change: ${0}".format(str(round(average_change, 2))) + "\n")
    result.write("Greatest Increase in Profits: {0} (${1})".format(max_month_profit, str(round(max_profit))) + "\n")
    result.write("Greatest Decrease in Profits: {0} (${1})".format(min_month_profit, str(round(min_profit))) + "\n")