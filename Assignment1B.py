print(f"[Ideal Gas Law Calculator]")
moles = float(input("Enter the number of moles of the gas: "))
tempC = float(input("Enter the temperature of the gas in Celsius: "))
volume = float(input("Enter the volume of the gas in Liters: "))
tempK = tempC+273.15
R = 0.0821
pressure = round((moles*R*tempK)/volume,2)
print(f"\nThe pressure of the gas is {pressure} atm")