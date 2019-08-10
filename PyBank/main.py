import csv
import os
PyBank_csv = os.path.join("/System/Volumes/Data/Users/eilishboyd$/class/COLNYC20190716DATA/02-Homeworks/03-Python/Instructions/PyBank/Resources/budget_data.csv)
with open(PyBank_csv, newline=") as PyBank_csv:
  csvreader = csv.reader(PyBank_csv, delimiter=',')
  csv_header = next(csvreader)
          
  profit = []
  date = []
  monthly_changes = []
          
          count = 0
          total_profit = 0
          total_change = 0
          prev_profit = 0
          
          for row in csvreader:
          count = count + 1
       date.append(row[0])
          
          
       profit.append(row[1])
       total_profit = total_profit + int(row[1])
          
          
       final_profit = int(row[1])
       monthly_profit_change = final_profit - prev_profit
          
      
          
       monthly_changes.append(monthly_profit_change)
       total_change = total_change + monthly_profit_change
       prev_profit = final_profit
       avg_change_profit = (total_change/count)
       greatest_increase = max(monthly_changes)
       greatest_decrease = min(monthly_changes)
       increase_date = date[monthly_changes.index(greatest_increase)]
       decrease_date = date[monthly_changes.index(greatest_decrease)]
       print(“Financial Analysis”)
       print(“Total Months:” + str(count))
          
       print "Total Revenue: $[total_months}\n"
       print(“Total Profits:” + “$” + str(total_profit))
       print(“Average Change:” ${revenue_avg}\n"
       print "Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
       print “Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
             
             print(output)
             with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
