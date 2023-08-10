def pal_function():    
    from pathlib import Path
    import csv

    day = []
    profit_and_loss = []
    profit_deficit = []


    fcoh = Path.cwd()/"csv_reports"/"Profits_and_loss.csv"
    with fcoh.open(mode="r", encoding="UTF-8") as file:
                reader = csv.reader(file)
                next(reader)

                for row in reader:
                        day.append(row[0])
                        profit_and_loss.append(row[5])


    for i in range(len(profit_and_loss)):
                if i < len(profit_and_loss)-1:
                    if int(profit_and_loss[i]) > int(profit_and_loss [i+1]):
                        deficit = int(profit_and_loss[i]) - int(profit_and_loss[i+1])
                        
                        print(f"[NET PROFIT DEFICIT]: DAY: {day[i+1]}, AMOUNT: USD{deficit}")
                        profit_deficit.append(f"[NET PROFIT DEFICIT]: DAY: {day[i+1]}, AMOUNT: USD{deficit}\n")



    max_surplus = 0
    highest_profit_surplus = []
    for i in range(len(profit_and_loss)):
                if i < len(profit_and_loss)-1:
                    if int(profit_and_loss[i+1]) > int(profit_and_loss[i]):
                        surplus = int(profit_and_loss[i+1]) - int(profit_and_loss[i])
                        day = i

                        if day == 0:
                            continue
                            
                        else:
                            if surplus > max_surplus:
                                max_surplus = surplus
                                max_day = day + 1

                            else:
                                continue
                    
    print(f"[HIGHEST NET PROFIT SURPLUS]: DAY: {max_day}, AMOUNT: USD{max_surplus}")
    highest_profit_surplus.append(f"[HIGHEST NET PROFIT SURPLUS]: DAY: {max_day}, AMOUNT: USD{max_surplus}\n")
    return(highest_profit_surplus, profit_deficit)


pal_function()