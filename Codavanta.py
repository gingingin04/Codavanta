# Declaration and input of variables

gravity = 9.81
pi = 22/7

mass = float(input('''Enter your mass
          Mass is the All Up Weight, Total mass including batteries in Grams
          : '''))
weight = mass * gravity  # gravitational acceleration = 9.81
thrust50 = float(input('''Enter your thrust at 50% throttle
          Please check the data sheet
          : '''))
thrust100 = float(input('''Enter your thrust at 100% throttle
          Please check the data sheet
          : '''))
prop_dim = float(input('''Enter your prop size unit
                       1. in mm
                       2. in inches
                       : '''))
   if prop_dim == 1:
        prop_diameter = float(input('''Enter your propellor size in mm
        : '''))
    elif prop_dim == 2:
        prop_diameter = float(input(''' Enter your propellor size in inches
        :'''))
    else:
        print("you did not put in the right value")

prop_num = float(input('''Enter your propellor number
          : '''))

print(mass)
print(thrust50)
print(thrust100)
print(prop_diameter)


# Hover Throttle % (Battery voltage Equation)

# Thrust to Weight Ratio(Y)
thrustweightratio50 = thrust50/weight
thrustweightratio100 = thrust100/weight

# Disk Loading (D)
diskload = (mass * gravity) / ((prop_num * pi * (prop_diameter / 2) ** 2))

print("the diskload is", diskload, "it is in grams per inch")

if 6 <= diskload <= 9:
    print("this is a freestyle quad")

else:
    print("this is not a freestyle quad")

# Tip Mach value(Y)

# Power Draw @ Hover and Cruising (D)


# Motor Torque VS Prop Inertia match
