from pathlib import Path

file_path = Path.cwd()/"summary_report.txt"
file_path.touch()


import cash_on_hand, overheads, profit_loss

def main():

    highest_cash_surplus, cash_deficit =  cash_on_hand.coh_function()
    maxoh = overheads.overheads_function()
    highest_profit_surplus, profit_deficit = profit_loss.pal_function()
    return(highest_cash_surplus, cash_deficit, highest_profit_surplus, profit_deficit, maxoh)
  
    

highest_cash_surplus, cash_deficit, highest_profit_surplus, profit_deficit, maxoh = main()

main()


with file_path.open(mode='w', encoding='UTF-8') as file:
    file.writelines(cash_deficit)
    file.writelines(highest_cash_surplus)
    file.writelines(profit_deficit)
    file.writelines(highest_profit_surplus)
    file.writelines(maxoh)
