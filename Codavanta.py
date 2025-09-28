# Declaration and input of variables

gravity = 9.81
pi = 22/7
a = 343  # speed of sound in m/s
freestyle = 0
cinematic = 0
long_range = 0
racing = 0

mass = float(input('''Enter your mass
          Mass is the All Up Weight, Total mass including batteries in \033[1mGrams\033[0m
          : '''))
kg_mass = mass / 1000

weight = kg_mass * gravity  # gravitational acceleration = 9.81
thrust50 = float(input('''Enter your thrust at 50% throttle in \033[1mNewtons\033[0m
          Please check the data sheet
          : '''))
thrust100 = float(input('''Enter your thrust at 100% throttle \033[1mNewtons\033[0m
          Please check the data sheet
          : '''))
prop_unit = float(input('''Enter your prop size unit
                       1. in \033[1mmm\033[0m
                       2. in \033[1minches\033[0m
                       : '''))


if prop_unit == 1:
    print("prop unit will be calculated in \033[1mmm\033[0m")
    prop_diameter = float(input("Enter prop diameter: "))
elif prop_unit == 2:
    print("prop unit will be calulctaed in \033[1minches\033[0m")
    prop_diameter = float(input("Enter prop diameter: "))
else:
    print("no clue what this is")

prop_num = float(input('''Enter your propellor blade number
          : '''))

motor_kv = float(input('''Enter your motor \033[1mkv\033[0m
          : '''))

battery_cell_count = float(input('''Enter your Lipo cell count
          : '''))

battery_voltage = battery_cell_count * 3.8

rpm = motor_kv * battery_voltage

amp_draw_hover = float(input(f"What is the amp draw @ {mass / 4} grams? "))

Power_draw_hover = battery_voltage * amp_draw_hover

print(kg_mass)
print(thrust50)
print(thrust100)
print(prop_unit)
print(motor_kv)
print(amp_draw_hover)
print(Power_draw_hover)
print()

# Hover Throttle % (Battery voltage Equation)

# Thrust to Weight Ratio(Y)
print()
thrustweightratio50 = thrust50/weight
print("the thrust to weight ratio at 50% throttle is", thrustweightratio50)
thrustweightratio100 = thrust100/weight
print("the thrust to weight ratio at 100% throttle is", thrustweightratio100)
if thrustweightratio50 == 2:
    print("this is a long range quad")
elif thrustweightratio50 > 2 and thrustweightratio50 < 3:
    print("this is a cenimatic quad")
elif thrustweightratio50 >= 3 and thrustweightratio50 < 4:
    print("this is a freestyle quad")
elif thrustweightratio50 >= 4:
    print("this is a racing quad")
print()

# Disk Loading (D)
print()
mm_to_inch = 0.0393701

if prop_unit == 1:
    prop_diameter = prop_diameter / 1000
else:
    prop_diameter = (prop_diameter * 25.4) / 1000


diskload = (kg_mass) / ((prop_num * pi * (prop_diameter / 2) ** 2))

print("the diskload is", diskload,
      "it is in \033[1mkilograms per meter sqrd\033[0m")
print(prop_diameter)

if 6 <= diskload <= 8.5:
    print("this is a long range quad")
    long_range += 1
elif 8.5 < diskload <= 11:
    print("this is a racing quad")
    racing += 1
elif 11 < diskload < 16:
    print("this is a freestyle quad")
    freestyle += 1
elif 16 <= diskload:
    print("this is a cinematic quad")
    cinematic += 1
print()

# Tip Mach value(Y)
print()
V_tip = (rpm / 60) * prop_diameter * pi
M_tip = V_tip / a
print("the tip mach value is", M_tip)
if 0.6 <= M_tip <= 0.9:
    print("this is a freestyle quad")
    freestyle += 1
elif 0.15 < M_tip <= 0.3:
    print("this is a long range or a cinematic quad")
    long_range += 1
    cinematic += 1
elif 0.3 < M_tip <= 0.6:
    print("this is a racing quad")
    racing += 1
print()
# Power Draw @ Hover and Cruising (D)
print()

print(f"Powerdraw at hover is {Power_draw_hover} watts")

print()
# Motor Torque VS Prop Inertia match (Y)
print()
motor_torque = Power_draw_hover / (rpm * (2 * pi / 60))

print()
