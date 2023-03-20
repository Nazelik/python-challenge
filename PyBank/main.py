import os
import csv

# total number of months
total_months = 0

# total amount of profit/losses over entire period
total_prof_loss = 0

# profit/losses value of last iteration
last_profit = 0

# average of changes of profit/losses
average_change = 0

# store csv file header
header = ""

# greatest increase in profits
max = 0

# date of greatest increase 
max_date = 0

# greatest decrease in profits
min = 0 

# date of greatest decrease 
min_date = 0

# path where output file will be created
parent_path = "./analysis"

# file path to read the data from
budget_csv = os.path.join(".", "Resources", "budget_data.csv")

# if not exists, create  "analysis" directory 
if (not os.path.exists(parent_path)):
    os.mkdir(parent_path)
    

# file path to write to
output_path = os.path.join(".", "analysis", "output.txt")

# Open the file using "write" mode. 
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    # skip the header
    header = next(csv_file)

    # Read through each row of data after the header
    for row in csv_reader:
        # The first element in the csv list is not a change, so exclude it.
        if total_months == 0:
            last_profit = int(row[1])

        total_prof_loss = total_prof_loss + int(row[1])
        total_months = total_months + 1
        change = int(row[1]) - last_profit        
        average_change = average_change + change
        last_profit = int(row[1])

        # Carry min and max values of changes, to not have extra loop for this.
        if change > max:
            max = change
            max_date = row[0]
        if change < min:
            min = change
            min_date = row[0] 

average_change = round((average_change/(total_months - 1)), 2)

# Open a new file using "write" mode
with open(output_path, 'w') as file_w:
    #print("'output.txt' file is created.")
    file_w.write("Financial Analysis" + "\n")
    file_w.write("------------------" + "\n")
    file_w.write(""+ "\n")
    file_w.write(f"Total Months: {total_months} \n")
    file_w.write(f"Total: ${total_prof_loss}\n")
    file_w.write(f"Average Change: ${average_change}\n")
    file_w.write(f"Greatest Increase in Profits: {max_date} (${max})\n")
    file_w.write(f"Greatest Decrease in Profits: {min_date} (${min})\n")
print()
print("Financial Analysis")    
print("--------------------")
print()
print(f"Total Months: {total_months}")
print(f"Total: ${total_prof_loss}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {max_date} (${max})")
print(f"Greatest Decrease in Profits: {min_date} (${min})\n")
