from enums.enums import InventoryFirstTableEnum
import numpy as np
import random



class Solver :
  def __init__(self):
    self.order_quantity = 10
    self.reorder_point = 5
    self.recived_lead = 0
    self.onOrder = False
  
  def calculate_first_table(self ,frequency ,table_type):
      table = self.init_first_empety_table(table_type)
      counter = 0
      cumulative = 0
      last_interval = 0
      for frequency_row in frequency:
        if table_type == "DEMAND":
          table[table_type].append(counter)
        elif table_type == "LEAD":
          table[table_type].append(counter+1)
        table["FREQUENCE"].append(frequency_row)
        probability = round(frequency_row / np.sum(frequency),2)
        table["PROBABILITY"].append(probability)
        cumulative += round(probability,2)
        table["CUMULATIVEP_ROBABILITY"].append(cumulative)
        interval = (last_interval + 1 , (cumulative * 100) )
        last_interval =  (cumulative * 100)
        table["INTERVAL_OF_RANDOM_NUMBERS"].append(interval)
        counter += 1
      return table
      
      
      
      
  def init_first_empety_table(self ,table_type):
      return {
          table_type : [] ,
          "FREQUENCE" : [] ,
          "PROBABILITY" : [] ,
          "CUMULATIVEP_ROBABILITY" : [] ,
          "INTERVAL_OF_RANDOM_NUMBERS" : [] 
          
      }
      
    
  def solver (self ,demand_table , lead_table , day_count):
      
      table = self.init_output_table()
      self.fill_output_first_row(table , demand_table , lead_table)
      for day in range(1,day_count):
        table['DAY'].append(day+1)
        self.set_beginning(table)
        table["DEMAND_RANDOM_NUMBER"].append(random.randint(1,100))
        table["DEMAND"].append(self.get_demand_from_random_number(table["DEMAND_RANDOM_NUMBER"][-1] , demand_table ))
        self.set_ending_lost(table)    
        is_need_order_var = self.is_need_order(table)
        if is_need_order_var :
          self.onOrder = True
          table["ORDER"].append('yes')
          table["LEAD_RANDOM_NUMBER"].append(random.randint(1,100))
          table["LEAD_TIME"].append(self.get_lead_from_random_number(table["LEAD_RANDOM_NUMBER"][-1] , lead_table ))
        else :
          table["ORDER"].append('no')
          table["LEAD_RANDOM_NUMBER"].append(0)
          table["LEAD_TIME"].append(0)
      return table
    
    
    
  def init_output_table(self):
    
    return {
      
            "DAY" : [],
            "UNIT_RECEIVED" : [] ,
            "BEGINNING_INVENTORY" : [] ,
            "DEMAND_RANDOM_NUMBER" : [] ,
            "DEMAND" : [] ,
            "ENDING_INVENTORY" : [] ,
            "LOST_SALES" : [] ,
            "ORDER" : [] ,
            "LEAD_RANDOM_NUMBER" : [] ,
            "LEAD_TIME" : [] 
            
        }
    
  def fill_output_first_row(self ,table , demand_table , lead_table):
    table['DAY'].append(1)
    self.set_beginning(table)
    table["DEMAND_RANDOM_NUMBER"].append(random.randint(1,100))
    table["DEMAND"].append(self.get_demand_from_random_number(table["DEMAND_RANDOM_NUMBER"][-1] , demand_table ))
    self.set_ending_lost(table)    
    is_need_order_var = self.is_need_order(table)
    if is_need_order_var :
      self.onOrder = True
      table["ORDER"].append('yes')
      table["LEAD_RANDOM_NUMBER"].append(random.randint(1,100))
      table["LEAD_TIME"].append(self.get_lead_from_random_number(table["LEAD_RANDOM_NUMBER"][-1] , lead_table ))
    else :
      table["ORDER"].append('no')
      table["LEAD_RANDOM_NUMBER"].append(0)
      table["LEAD_TIME"].append(0)
  
    
    

  def is_need_order(self ,table):
    
      return ( (table["BEGINNING_INVENTORY"][-1] < table["DEMAND"][-1] ) or ( table["BEGINNING_INVENTORY"][-1] <=  self.reorder_point) ) and not self.onOrder
    

  def get_demand_from_random_number(self ,random , demand_table):
    index = 0
    for (x,y) in demand_table['INTERVAL_OF_RANDOM_NUMBERS']:
      if random >= x and random <= y:
        return demand_table['DEMAND'][index]
      index += 1
        
    
  def get_lead_from_random_number(self ,random , lead_table):
    index = 0
    for (x,y) in lead_table['INTERVAL_OF_RANDOM_NUMBERS']:
      if random >= x and random <= y:
        self.recived_lead = lead_table['LEAD'][index]
        return self.recived_lead
      index += 1
        
    
  def set_beginning(self,table):
    if len(table['BEGINNING_INVENTORY']) == 0 :
      table['BEGINNING_INVENTORY'].append( self.order_quantity)
      table["UNIT_RECEIVED"].append(0)
    else :
      beginning =  table['ENDING_INVENTORY'][-1]
      if self.is_recive_order():
        table["UNIT_RECEIVED"].append( self.order_quantity)
        beginning +=  self.order_quantity
      else :
        table["UNIT_RECEIVED"].append(0)
      table['BEGINNING_INVENTORY'].append(beginning)


  def is_recive_order(self):
    if self.recived_lead > 0 and self.onOrder == True :
      self.recived_lead -= 1
    elif self.recived_lead == 0 and self.onOrder == True:
      self.onOrder = False
      return True
    return False
      
  def set_ending_lost(self ,table):
    
    if table["BEGINNING_INVENTORY"][-1] > table["DEMAND"][-1] :
      table["ENDING_INVENTORY"].append(table["BEGINNING_INVENTORY"][-1] - table["DEMAND"][-1] )
      table["LOST_SALES"].append(0)
    elif table["BEGINNING_INVENTORY"][-1] == table["DEMAND"][-1]  :
      table["ENDING_INVENTORY"].append(0)
      table["LOST_SALES"].append(0)
    elif table["BEGINNING_INVENTORY"][-1] < table["DEMAND"][-1]  :
      table["ENDING_INVENTORY"].append(0)
      table["LOST_SALES"].append(table["DEMAND"][-1] - table["BEGINNING_INVENTORY"][-1] )