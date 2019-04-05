from tkinter import *
from enum import Enum
from views.Inventory.inventory_input import InventoryInput

class Algorithm(Enum):
    Inventory = 1
    Transprotation = 2    
     


class Menu:
    def __init__(self, master):
        self.master = master
        self.master.title("Simulation")
        self.frame = Frame(self.master)

        self.choise = Label(self.frame, text='Chose an algorithm')
        self.choise.grid(row=0, column=0)
        self.inventoryBtn = Button(self.frame , text='Inventory' , command=lambda :self.init_algorithm_view(Algorithm.Inventory))
        self.inventoryBtn.grid(row=2, column=0)
        self.transprotationBtn = Button(self.frame , text='Transprotation' , command=lambda :self.init_algorithm_view(Algorithm.Transprotation))
        self.transprotationBtn.grid(row=3, column=0)

        self.frame.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)

        self.frame.pack(pady=250)
        
    def init_algorithm_view(self , enum):
        if(enum == Algorithm.Inventory):
            self.frame.destroy()
            InventoryInput(self.master)
            
        elif (enum == Algorithm.Transprotation):
            print('tran')
            
        

  