units = 100  # Define the variable units with a value

if(units < 50):
    amount = units * 2.60
    surcharge = 25

elif(units <= 150):
    amount = 130 + ((units - 50) * 3.25)
    surcharge = 35

elif(units <= 200):
    amount = 130 + 162.50 +  ((units - 150) * 1.20)
    surcharge = 45

else:
    amount = 130 + 162.50 + 526 + ((units - 200) * 8.45)
    surcharge = 75

total = amount + surcharge
print("Electricity Bill: ", total)
