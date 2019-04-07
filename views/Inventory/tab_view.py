from tkinter import *
from enum import Enum
import pandas as pd 
from pandastable import Table, TableModel

  
# initialize list of lists 
data = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]] 
  
table_1_columns = ['Demand', 'Frequancy' , 'Probabilty' ,'cumulative Probabilty' , 'Interval']
df = pd.DataFrame(data, columns = table_1_columns) 
class InventoryOutputTabs:
    
    def __init__(self, master):
        self.master = master
        self.master.title("Simulation - Inventory")
        self.frame = Frame(self.master)
        self.table = pt = Table(self.frame, dataframe=df,
                                showtoolbar=True, showstatusbar=True)
        #self.table.grid(row=0, column=1)      
        pt.show()  
        self.frame.pack(pady=2)
