#region VEXcode Generated Robot Configuration
from vex import *

# Brain should be defined by default
brain=Brain()

ratio = GearSetting.RATIO_18_1
# Robot configuration code
left_motor_a = Motor(Ports.PORT1, ratio, False)
left_motor_b = Motor(Ports.PORT3, ratio, False)
left_drive_smart = MotorGroup(left_motor_a, left_motor_b)
right_motor_a = Motor(Ports.PORT4, ratio, True)
right_motor_b = Motor(Ports.PORT5, ratio, True)
right_drive_smart = MotorGroup(right_motor_a, right_motor_b)
controller_1 = Controller(PRIMARY)

# wait for rotation sensor to fully initialize
wait(30, MSEC)
#endregion VEXcode Generated Robot Configuration

# ------------------------------------------
# 
# Project:  Driver
#	Author: Driver
#	Created:
#	Description:  VEXcode V5 Python Project
# 
# ------------------------------------------

# Library imports
from vex import *

# Begin project code
while True:
    deadzone = 10
    stop = True
    right_axis = controller_1.axis2.position()
    left_axis = controller_1.axis3.position()
    if right_axis > deadzone:
        right_drive_smart.spin(FORWARD,right_axis)
        stop = False
    elif right_axis < -deadzone:    
        right_drive_smart.spin(FORWARD, right_axis)
        stop = False
    if left_axis > deadzone:
        left_drive_smart.spin(FORWARD, left_axis)
        stop = False
    elif left_axis < -deadzone:
        left_drive_smart.spin(FORWARD, left_axis)
        stop = False
    if stop:
        left_drive_smart.stop()
        right_drive_smart.stop()
