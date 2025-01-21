print(f"[Centimeters to Feet and Inches Converter]")
cm = float(input(f"Enter the length in centimeters: "))
ft = cm / 30.48
inch = round((ft % 1)*12,2)
ft = int(ft)
print(f"\nThe length is {ft} feet and {inch} inches")
