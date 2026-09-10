# Global Freight Calculator 

name = input("input name:") 
item= input("What is the item being shipped?") 
is_fragile = bool(input("It is fragile?")) 
weight = float(input("what is the weight of the Item?")) 
distance = float(input("what is the distance of the home?")) 
is_express = bool(input("is the Item is a express order? ")) 
is_international = bool(input("is the oreder is an international oreder? ")) 

#Calculataion of Base Cost 
base_cost = (weight *2.50) + (distance *0.15) 

#Evaluate Pricing Tiers 
#Apply the first matching conditions only 

if weight <= 2.0 and distance <= 100 and not is_express and not is_international: 
            total = 0 
elif is_international and is_express: 
            total = (base_cost *1.40) + 50 

elif is_express or (is_international and weight > 20): 
            total = (base_cost *1.20) + 25 

elif weight > 30 or distance < 1000: 
            total = base_cost * 30 
else: 
            total = base_cost 

print("\n---Resibo--->") 
print("Reciever:", name) 
print("Total Cost:", total)
