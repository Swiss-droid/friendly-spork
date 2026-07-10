print("Calculating The Unit Of Measurement")

unit = str(input("Enter the unit of measurement: "))
unit = float (input("Enter the length: "))

if unit == "Kilometres":
    "Miles" == "Kilometres" * 0.62137
elif "Metres" == "Kilometres" * 1000:
    print("This is true.")
elif "Centimetres" == "Kilometres" * 100000:
    print("This is true.")
elif "Millimetres" == "Kilometres" * 1000000:
    print("This is true.")
elif "Feet" == "Kilometres" * 3280.84 :      # 3280.8999
    print("This is true.")
else:
    print("That doesn't apply.")



if unit == "Miles":
    "Kilometres" == "Miles" * 1.609344
elif "Metres" == "Miles" * 1609.344:
    print("This is true.")
elif "Centimetres" == "Miles" * 160934.4:
    print("This is true.")
elif "Millimetres" == "Miles" * 1609344:
    print("Tis is true.")
elif "Feet" == "Miles" * 5280:
    print("This is true.")
else:
    print("That doesn't apply.")



if unit == "Centimetres":
    "Kilometres" == "Centimetres" * 0.00001
elif "Metres" == "Centimetres" * 0.01:
    print("This is true.")
elif "Miles" == "Centimetres" * 0.00000621:
    print("This is true.")
elif "Millimetres" == "Centimetres" * 10:
    print("This is true.")
elif "Feet" == "Centimetres" * 0.0328084:
    print("This is true.")
else:
    print("That doesn't apply.")


if unit == "Metres":
    "Kilometres" == "Metres" * 0.001
elif "Miles" == "Metres" * 0.00062137:
    print("Tis is true.")
elif "Centimetres" == "Metres" * 100:
    print("Tis is true.")
elif "Millimetres" == "Metres" * 1000:
    print("Tis is true.")
elif "Feet" == "Metres" * 3.2808399:
    print("Tis is true.") 
else:
    print("That doesn't apply.")


if unit == "Millimetres":
    "Kilometres" == "Millimetres" / 100000
elif "Miles" == "Millimetres" / 1.6093:
    print("This is true.")
elif "Metres" == "Millimetres" / 1000:
    print("This is true.")
elif "Centimetres" == "Millimetres" / 0.1:
    print("This is true.")
elif "Feet" == "Millimetres" / 0.00328084:
    print("This is true.")
else:
    print("That doesn't apply.")



if unit == "Feet":
    "Kilometres" == "Feet" * 0.0003048
elif "Miles" == "Feet" * 0.00018939:
    print("This is true.")
elif "Metres" == "Feet" * 0.3048:
    print("This is true.")
elif "Centimetres" == "Feet" * 30.48:
    print("This is true.")
elif "Millimetres" == "Feet" * 304.8:
    print("This is true.")
else:
    print("That doesn't apply.")


print("The answer is", unit)
print("Thank you!")
