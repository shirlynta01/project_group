def overheads_function():

    """
    This function calculates the highest overheads
    No parameter is required
    """

    from pathlib import Path
    import csv

    # create a file path
    file_path_read = Path.cwd()/'csv_reports'/'Overheads.csv'

    # read the csv file to append expense name and overheads data
    with file_path_read.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header

        # create an empty lists to store the type of expense and the overheads
        overheads=[] 
        expense_name = []

        # append type of expense and the overheads into the respective lists
        for row in reader:
            expense_name.append(row[0])
            overheads.append(row[1])

    # create an empty list to store the final output that is to be displayed in the txt file
    maxoh = []
    
    # create a variable that will store overheads data 
    max_overheads = 0

    # using for loop to iterate over the range of the overheads 
    for i in range(len(overheads)):

        # since the index of a list always starts from 0, therefore len(overheads)-1 to ensure index is in range of the list
        if i < len(overheads)-1:

            # float() function to convert data from string to float to use >
            overheads_value = float(overheads[i])
            count = i

            # if new overheads value > previous overheads value assigned to the max_overheads variable in the for loop,
            if overheads_value > max_overheads:

                # new overheads value will override the previous overheads value assigned and become the new value for the max_overheads variable.
                max_overheads = overheads_value

    # print highest overheads and the day using an f-string
    print(f'[Highest Overheads] {expense_name[count]}: {max_overheads}%')

    # append the desired output to a list
    maxoh.append(f'[Highest Overheads] {expense_name[count]}: {max_overheads}')

    return(maxoh)

# calling the function so that there is an output
overheads_function()
