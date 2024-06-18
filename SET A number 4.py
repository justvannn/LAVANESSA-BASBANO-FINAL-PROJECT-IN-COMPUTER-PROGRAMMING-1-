print('Number 4.')
def meters_to_feet(meters):
    feet = meters * 3.28084
    return feet

def feet_to_meters(feet):
    meters = feet / 3.28084
    return meters

print("Measurement Converter")
print("1. Meters to Feet")
print("2. Feet to Meters")

choice = input("Enter your choice (1/2): ")

if choice == '1':
    meters = float(input("Enter length in meters: "))
    feet = meters_to_feet(meters)
    print(f"{meters} meters is equal to {feet} feet.")
elif choice == '2':
    feet = float(input("Enter length in feet: "))
    meters = feet_to_meters(feet)
    print(f"{feet} feet is equal to {meters} meters.")
else:
    print("Invalid choice. Please enter 1 or 2.")

