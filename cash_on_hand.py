def coh_function():

    """
    This function calculates the cash deficit or highest cash surplus when there is no cash deficit
    No parameter required
    """    

    from pathlib import Path
    import csv


    # create empty lists to store day, cash on hand, cash deficit and highest cash surplus 
    day = []
    cash_on_hand = []
    cash_deficit = []
    deficit_list = []
    highest_cash_surplus = []
    # create a variable for max cash surplus and the day that the highest cash surplus occurs
    max_day = 0
    max_surplus = 0
    

    # create a file to csv file.
    fcoh = Path.cwd()/"csv_reports"/"Cash_on_Hand.csv"
    with fcoh.open(mode="r", encoding="UTF-8") as file:
        
        # read the csv file to append day and cash on hand from the csv.
        reader = csv.reader(file)
        next(reader) #skip header

        # append day and cash on hand into their respective lists
        for row in reader:

            day.append(row[0])
            cash_on_hand.append(row[1])


    # print deficit from day 0-90 if there are deficits
    # using for loop to iterate over the range of the days
    for i in range(len(cash_on_hand)):

        if i < len(cash_on_hand)-1:
            
            # if previous day's cash on hand is more than the current day
            if int(cash_on_hand[i]) > int(cash_on_hand [i+1]):
                
                # calculate deficit 
                deficit = int(cash_on_hand[i]) - int(cash_on_hand[i+1])

                # print out day and deficit using f-strings
                print(f"[CASH DEFICIT]: DAY: {day[i+1]}, AMOUNT: USD{deficit}")

                #append deficit into deficit list
                deficit_list.append(deficit)

                cash_deficit.append(f"[CASH DEFICIT]: DAY: {day[i+1]}, AMOUNT: USD{deficit}\n")

    

    # print max surplus if there are no deficits in the deficit list
    if deficit_list == []:

        # using for loop to iterate over the range of the days        
        for i in range(len(cash_on_hand)):
            
            # since the index of a list always starts from 0, therefore len(overheads)-1 to ensure index is in range of the list
            if i < len(cash_on_hand)-1:                

                # if current day's cash on hand is always more than the previous day
                if int(cash_on_hand[i+1]) > int(cash_on_hand[i]):
                    
                    # calculate surplus
                    surplus = int(cash_on_hand[i+1]) - int(cash_on_hand[i])
                    day = i 

                    # calculate highest surplus and the day that highest surplus occurred
                    if surplus > max_surplus:
                        max_surplus = surplus
                        max_day = day + 1

                    else:
                        continue
        
        #print highest cash surplus and the day with f-strings 
        print(f"[HIGHEST CASH SURPLUS]: DAY: {max_day}, AMOUNT: USD{max_surplus}")

        highest_cash_surplus.append(f"[HIGHEST CASH SURPLUS]: DAY: {max_day}, AMOUNT: USD{max_surplus}\n")
    
    return(highest_cash_surplus, cash_deficit)

# calling the function so that there is an output
coh_function()


        
