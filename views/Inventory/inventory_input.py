from tkinter import *
from enum import Enum


class InventoryInputTableKeys(Enum):
    Demand = "demand"
    Frequence = "frequence"

class InventoryInput:
    
     def __init__(self, master):
        self.master = master
        self.master.title("Simulation - Inventory")
        self.frame = Frame(self.master)
        self.row_count = 0
        self.input = dict()
        
        self.scrollbar = Scrollbar(self.master)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        
        self.frame.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)
        
        self.demandLbl = Label(self.frame ,text= "Demand")
        self.demandLbl.grid(row=0, column=0)
        self.demandLbl = Label(self.frame ,text= "Frequence")
        self.demandLbl.grid(row=0, column=1)
        self.append_input_row()
        
        
        
       

        self.frame.pack(pady=2)
        self.add_rowBtn = Button(self.master , text = "Simulate" ,command=lambda :self.append_input_row() )
        self.add_rowBtn.pack(side = BOTTOM , fill=X)
        self.add_rowBtn = Button(self.master , text = "Add row" ,command=lambda :self.append_input_row() )
        self.add_rowBtn.pack(side = BOTTOM , fill=X)
        
     def append_input_row(self):
        self.row_count +=1
        self.input[InventoryInputTableKeys.Demand] =dict()
        self.input[InventoryInputTableKeys.Frequence] = dict()
        self.input[InventoryInputTableKeys.Demand][self.row_count] = Entry(self.frame)
        self.input[InventoryInputTableKeys.Demand][self.row_count].insert(0,self.row_count-1)
        self.input[InventoryInputTableKeys.Demand][self.row_count].grid(row=self.row_count,column=0)
        self.input[InventoryInputTableKeys.Frequence][self.row_count] = Entry(self.frame)
        self.input[InventoryInputTableKeys.Frequence][self.row_count].grid(row=self.row_count,column=1)
            
     