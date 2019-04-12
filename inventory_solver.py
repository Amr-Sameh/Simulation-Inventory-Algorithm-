from enums.enums import InventoryFirstTableEnum
import numpy as np


def calculate_first_table(frequency):
    table = init_first_empety_table()
    counter = 0
    cumulative = 0
    last_interval = 0
    for frequency_row in frequency:
      table["DEMAND"].append(counter)
      table["FREQUENCE"].append(frequency_row)
      probability = round(frequency_row / np.sum(frequency),2)
      table["PROBABILITY"].append(probability)
      cumulative += probability
      table["CUMULATIVEP_ROBABILITY"].append(cumulative)
      interval = (last_interval + 1 , (cumulative * 100) )
      last_interval =  (cumulative * 100)
      table["INTERVAL_OF_RANDOM_NUMBERS"].append(interval)
    return table
    
    
    
    
    
    
def init_first_empety_table():
    return {
        "DEMAND" : [] ,
        "FREQUENCE" : [] ,
        "PROBABILITY" : [] ,
        "CUMULATIVEP_ROBABILITY" : [] ,
        "INTERVAL_OF_RANDOM_NUMBERS" : [] 
        
    }
    
