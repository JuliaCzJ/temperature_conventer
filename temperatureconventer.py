unit = input("Is this temperature in Celsjus or Fahrenheit? (C/F): ")
temperature = float(input("Enter the temperature: "))

if unit == "C":
    temperature = round((temperature * 9) / 5 + 32, 1)
    unit = "Fahrenheit"
    print(f"Your temperature is {temperature} {unit}")
elif unit == "F":
    temperature = round((temperature - 32) * 5 / 9, 1)
    unit = "Celsius"
    print(f"Your temperature is {temperature} {unit}")
else:
    print("Mistake, put right units or temperature sign")