from tkinter import *
from tkinter import ttk
from enum import Enum
import pandas as pd 
from pandastable import Table, TableModel
from inventory_solver import calculate_first_table

  
# initialize list of lists 
data2 = [[1,2,4,5,6],[1,2,3,6,6],[1,2,6,6,3],[1,2,6,6,3],[1,2,6,6,3],[1,2,6,6,3]] 
  
table_1_columns = ['Demand', 'Frequancy' , 'Probabilty' ,'cumulative Probabilty' , 'Interval']

df2 = pd.DataFrame(data2, columns = table_1_columns) 

class InventoryOutputTabs:
    
    def __init__(self, master,data):
        self.master = master
        self.master.title("Simulation - Inventory")
        self.tab_manager = ttk.Notebook(self.master)
        first_table_data = calculate_first_table(data)
        df = pd.DataFrame(first_table_data)
        self.output_1_frame = self.render_table(df)
        self.output_2_frame = self.render_table(df2)
        self.tab_manager.add(self.output_1_frame, text="output 1")
        self.tab_manager.add(self.output_2_frame, text="output 2")
        self.tab_manager.pack(pady=2)
        
        
    def render_table(self , df):
        output_frame = Frame(self.master)
        output_table = Table(output_frame, dataframe=df,
                                showtoolbar=True, showstatusbar=True)
        output_table.show() 
        return output_frame 
        