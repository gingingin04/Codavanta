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

prop_diameter = float(input('''Enter your propellor size in inches
          At this stage, we are not taking into account the number of blades on the props
          : '''))


# Hover Throttle % (Battery voltage Equation)

# Thrust to Weight Ratio(Y)
thrustweightratio50 = thrust50/weight
thrustweightratio100 = thrust100/weight

# Disk Loading (D)
diskload = (mass * gravity) / ((4 * pi * (prop_diameter / 2) ** 2))

# Tip Mach value(Y)

# Power Draw @ Hover and Cruising (D)


# Motor Torque VS Prop Inertia match
