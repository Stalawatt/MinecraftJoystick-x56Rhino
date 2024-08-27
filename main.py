import pygame.joystick as pg,pydirectinput as input, pygame, pynput, threading

pg.init()
pygame.init()

input.FAILSAFE = False

mouse = pynput.mouse.Controller()

# Axis - Stick:
# 0 - Left And Right
# 1 - Forward And Backward
# 2 - ThumbStick L and R
# 3 - ThumbStick F and B
# 4 - Rotation / Rudders

# Axis - Throttle :
# 0 - Unknown
# 1 - Throttle Control 

# Stick Axis 0 and 1 for looking around / mouse movement
# Throttle Axis 1 for movement (forward/back)

# Buttons - Stick:
# 0 - Trigger
# 1 - A button between dpads
# 2 - Side Button
# 3 - C axis push in
# 4 - Pinky Button
# 5 - Pinky Trigger 
 

if pg.get_init():
    Stick = pg.Joystick(0)
    Throttle = pg.Joystick(1)
    Stick.init()
    Throttle.init()
    print("Initialisation Complete")
    


print("Starting")

def axisControls():


    while True:
        events = pygame.event.get()
        if len(events) != 0:
            event = events[len(events)-1]

        if event.type == pygame.JOYAXISMOTION:
            if Throttle.get_axis(1) < -0.5 :
                input.keyDown("w")
            elif Throttle.get_axis(1) > 0.5 :
                input.keyDown("s")
            elif abs(Throttle.get_axis(1)) < 0.5 :
                input.keyUp("w")
                input.keyUp("s")
            
            # Look Left And Right
            if Stick.get_axis(0) > 0.3:
                mouse.move(45,0)
            elif Stick.get_axis(0) < -0.3:
                mouse.move(-45,0)
            
            # Look up and Down
            if Stick.get_axis(1) > 0.3:
                mouse.move(0,-30)
            elif Stick.get_axis(1) < -0.3:
                mouse.move(0,30)
            
            
        

def buttonControls():
    while True:
        for each in pygame.event.get():
            if each.type == pygame.JOYBUTTONDOWN:
                if Stick.get_button(0) == 1:
                    input.click()
                if Stick.get_button(1) == 1: 
                    mouse.scroll(0,-1)
                if Stick.get_button(2) == 1:
                    input.press("e")
                if Stick.get_button(3) == 1:
                    pass
                if Stick.get_button(4) == 1:
                    input.rightClick()

                if Throttle.get_button(0) == 1:
                    input.press("space")


axis = threading.Thread(target= axisControls)
buttons = threading.Thread(target= buttonControls)

axis.start()
buttons.start()