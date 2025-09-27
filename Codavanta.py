# Declaration and input of variables

gravity = 9.81
pi = 22/7

mass = float(input('''Enter your mass
          Mass is the All Up Weight, Total mass including batteries in Grams
          : '''))
kg_mass = mass / 1000

weight = mass * gravity  # gravitational acceleration = 9.81
thrust50 = float(input('''Enter your thrust at 50% throttle
          Please check the data sheet
          : '''))
thrust100 = float(input('''Enter your thrust at 100% throttle
          Please check the data sheet
          : '''))
prop_unit = float(input('''Enter your prop size unit
                       1. in mm
                       2. in inches
                       : '''))

if prop_unit == 1:
    print("prop unit will be calculated in mm")
    prop_diameter = float(input("Enter prop diameter: "))
elif prop_unit == 2:
    print("prop unit will be calulctaed in inches")
    prop_diameter = float(input("Enter prop diameter: "))
else:
    print("no clue what this is")

prop_num = float(input('''Enter your propellor blade number
          : '''))

print(kg_mass)
print(thrust50)
print(thrust100)
print(prop_unit)


# Hover Throttle % (Battery voltage Equation)

# Thrust to Weight Ratio(Y)
thrustweightratio50 = thrust50/weight
thrustweightratio100 = thrust100/weight

# Disk Loading (D)

mm_to_inch = 0.0393701

if prop_unit == 1:
    prop_diameter = prop_diameter
else:
    prop_diameter = (prop_unit * 25.4) / 1000

diskload = (kg_mass * gravity) / ((pi * (prop_diameter / 2) ** 2))

print("the diskload is", diskload, "it is in grams per inch")
print(prop_diameter)

if 6 <= diskload <= 9:
    print("this is a freestyle quad")

else:
    print("this is not a freestyle quad")

# Tip Mach value(Y)

# Power Draw @ Hover and Cruising (D)


# Motor Torque VS Prop Inertia match
