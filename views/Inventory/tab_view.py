from tkinter import *
from tkinter import ttk
from enum import Enum
import pandas as pd 
from pandastable import Table, TableModel
from inventory_solver import Solver

  
# initialize list of lists 
order_quantity = 10
reorder_point = 5
amr = -2


class InventoryOutputTabs:
    
    def __init__(self, master,demand_table , lead_table):
        self.master = master
        self.solver = Solver()
        self.demand_table = demand_table
        self.lead_table = lead_table
        self.master.title("Simulation - Inventory")
        self.tab_manager = ttk.Notebook(self.master)
        self.demand_table = self.solver.calculate_first_table(self.demand_table , "DEMAND")
        df = pd.DataFrame(self.demand_table)
        self.output_1_frame = self.render_table(df)
        self.lead_table = self.solver.calculate_first_table( self.lead_table,"LEAD")
        df = pd.DataFrame(self.lead_table)
        self.output_2_frame = self.render_table(df)
        self.output_table_data = self.solver.solver(self.demand_table , self.lead_table , 10)
        df = pd.DataFrame(self.output_table_data)
        self.output_3_frame = self.render_table(df)
        self.tab_manager.add(self.output_1_frame, text="step 1")
        self.tab_manager.add(self.output_2_frame, text="step 2")
        self.tab_manager.add(self.output_3_frame, text="step 3")
       # self.tab_manager.add(self.output_2_frame, text="step 3")
        self.tab_manager.pack(pady=2)
        
        
    def render_table(self , df):
        output_frame = Frame(self.master)
        output_table = Table(output_frame, dataframe=df,
                                showtoolbar=True, showstatusbar=True , width=600)
        output_table.show() 
        return output_frame 
        