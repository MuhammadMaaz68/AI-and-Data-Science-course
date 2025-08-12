temp = float(input("Enter Temprature in Celcius: "))

if temp < 0:
    print("Temprature is Freezing")

elif temp > 0 and temp <26:
    print("Temprature is Moderate")

elif temp > 26:
    print("Temprature is Hot")
