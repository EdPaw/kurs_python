#user to input variables
distance = float(input("Enter distance in km: "))
consumption = float(input("Enter fuel consumption per 100 km: "))
gas_price = float(input("Enter gas price per liter: "))

#calculate cost
cost = ((distance * consumption)/100) * gas_price

#print cost
print("Your trip cost is: ", cost)








