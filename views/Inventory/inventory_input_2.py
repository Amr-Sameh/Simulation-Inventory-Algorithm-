from tkinter import *
from views.Inventory.tab_view import InventoryOutputTabs
from enums.enums import InventoryFirstTableEnum



class InventoryInput2:
    
     def __init__(self, master , data1):
        self.master = master
        self.master.title("Simulation - Inventory")
        self.frame = Frame(self.master)
        self.row_count = 0
        self.input = list()
        self.data1 = data1
        
        
        
        self.frame.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)
        
        self.demandLbl = Label(self.frame ,text= "Lead Time")
        self.demandLbl.grid(row=0, column=0)
        self.demandLbl = Label(self.frame ,text= "Frequence")
        self.demandLbl.grid(row=0, column=1)
        self.append_input_row()
        
        
        
       

        self.frame.pack(pady=2)
  
        self.add_rowBtn = Button(self.master , text = "Add row" ,command=lambda :self.append_input_row() )
        self.add_rowBtn.pack(side = BOTTOM , fill=X)
        self.simulateBtn = Button(self.master , text = "Simulate" ,command=lambda :self.show_output() )
        self.simulateBtn.pack(side = BOTTOM , fill=X)
        
     def append_input_row(self):
        self.row_count +=1
        entery = Entry(self.frame)
        entery.insert(0, str(self.row_count))
        entery.grid(row=self.row_count,column=0)
        entery = Entry(self.frame)
        self.input.append(entery)
        entery.grid(row=self.row_count,column=1)
        
     def show_output(self):
         data2 = self.featch_input()
         self.destroy_view()
         InventoryOutputTabs(self.master ,self.data1, data2)
         
         
     def destroy_view(self):
         self.frame.destroy()
         self.simulateBtn.destroy()
         self.add_rowBtn.destroy()
         
         
     def featch_input(self):
       data = list()
       for i in self.input:
          data.append(int(i.get()))
       return data            
     