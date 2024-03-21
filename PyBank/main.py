import os
import csv

pybank_csv_path = os.path.join("Resources", "budget_data.csv")

#csv_math will define variables and iterate through the csv to update the variabels and lists and finally return the values at the end
def csv_math():
    with open(pybank_csv_path, encoding = "UTF-8") as pybank_csv:
        csvreader = csv.reader(pybank_csv, delimiter = ",")
        csvheader = next(csvreader)
        #Here I am initializing the variables I will use and gather, except for income, which I define later
        row_counter = 0
        net_income = 0
        monthly_change = []
        monthly_change_date = []
        last_month_profit = None
        avg_change = ""
        max_profit = -1000 
        max_profit_month = ""
        min_profit = 1000 
        min_profit_month = ""

        #This is the only way I can find to consitantly skip the header. I would need to change this if the data or CSV I am importing does not have a header row
        #maybe another if function to check if row[1] = int:
        ## But I coullnt not get this if function to work. It seems like it cant do the if function by checking if row[1] is an integer value
        next(csvreader)

#the failed code is below

                # for row in csvreader:
        #     if last_month_profit != False:
        #         last_month_profit = row[1]
        #         monthly_change.append(row[1] - int(last_month_profit))
        #     last_month_profit = int(row[1])
            # if int(row[1]) > int(max_profit):
            #     max_profit = int(row[1])
            #     max_profit_month = row[0]
            # if int(row[1]) < min_profit:
            #     min_profit = int(row[1])
            #     min_profit_month = row[0]


        for row in csvreader:
            row_counter = row_counter +1
            income = int(row[1])
            if last_month_profit != None:
                #checking to see if there was a previous month
                monthly_change.append(income - last_month_profit)
                monthly_change_date.append(row[0])
                #Then after checking, we can update this as the future last_month_profit
                last_month_profit = int(row[1])
            else:
                last_month_profit = int(row[1])

            net_income = net_income + income

#max calculations
    max_profit = max(monthly_change)
    max_profit_index = monthly_change.index(max_profit)
    max_profit_month = monthly_change_date[max_profit_index]
#min calculations
    min_profit = min(monthly_change)
    min_profit_index = monthly_change.index(min_profit)
    min_profit_month = monthly_change_date[min_profit_index]

    if len(monthly_change) != 0:
        #calculate the monthly change and ensure we are not dividing by 0
        avg_change = sum(monthly_change) / len(monthly_change)
    #returning all relevent variables to use outside the function
    return row_counter, net_income, avg_change, max_profit, max_profit_month, min_profit, min_profit_month, monthly_change

#The profit_analysis function will use the returned values from csv_math as arguments, and print them for the user. It will then return these results to output them as an independent file
def profit_analysis(row_counter, net_income, avg_change, max_profit, max_profit_month, min_profit, min_profit_month):
    results =(f"""
Here is the Financial Information you requested
          
-----------------------------------------------

Total Months: {row_counter}
Net Income: $({net_income})
Average Month to Month Change: $({avg_change})
Greatest Increase in Profits: {max_profit_month} for $({max_profit})
Greatest Decrease in Profits: {min_profit_month} for $({min_profit})
          
          """)
    print(results)
    return results
    
#calling the fucntions
row_counter, net_income, avg_change, max_profit, max_profit_month, min_profit, min_profit_month, monthly_change = csv_math()
profit_analysis(row_counter, net_income, avg_change, max_profit, max_profit_month, min_profit, min_profit_month)

#This is declaring the path where I would like the results printed in a txt file for easy viewing
results = profit_analysis(row_counter, net_income, avg_change, max_profit, max_profit_month, min_profit, min_profit_month)
result_output_path = os.path.join("analysis", "Pybank_results.txt")
with open(result_output_path, "w") as Pybank_results:
    Pybank_results.write(results)

