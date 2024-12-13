import pyautogui

#################################################################
#                   get & Gather Information                    #
#################################################################

# Get the size of the primary monitor
screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)  # Example Output: (2560, 1440)

# Get the XY position of the mouse
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)  # Example Output: (1314, 345)

# True if x & y are within the screen.
pyautogui.onScreen(x, y)  # True

# Fail Safe
# Set up a 2.5 second pause after each PyAutoGUI call
pyautogui.PAUSE = 2.5

pyautogui.FAILSAFE = True

#################################################################
#                        Mouse Operation                        #
#################################################################

# Move the mouse to XY coordinates
pyautogui.moveTo(100, 150)
pyautogui.moveTo(x, y, duration=num_seconds)  # move mouse to XY coordinates over num_second seconds
pyautogui.moveRel(xOffset, yOffset, duration=num_seconds)  # move mouse relative to its current position

pyautogui.dragTo(x, y, duration=num_seconds)  # drag mouse to XY
pyautogui.dragRel(xOffset, yOffset, duration=num_seconds)  # drag mouse relative to its current position

pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left') # button=['left', 'middle', 'right']
pyautogui.rightClick(x=moveToX, y=moveToY)
pyautogui.middleClick(x=moveToX, y=moveToY)
pyautogui.doubleClick(x=moveToX, y=moveToY)
pyautogui.tripleClick(x=moveToX, y=moveToY)

pyautogui.scroll(amount_to_scroll, x=moveToX, y=moveToY)

pyautogui.mouseDown(x=moveToX, y=moveToY, button='left')
pyautogui.mouseUp(x=moveToX, y=moveToY, button='left')

# Click the mouse
pyautogui.click()
# Move the mouse to XY coordinates and click it
pyautogui.click(100, 200)

# Find where button.png appears on the screen and click it
pyautogui.click('button.png')

# Move the mouse 400 pixels to the right of its current position
pyautogui.move(400, 0)

# Double click the mouse
pyautogui.doubleClick()

# Use tweening/easing function to move mouse over 2 seconds
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)

#################################################################
#                      Keyboard Operation                       #
#################################################################

pyautogui.typewrite('Hello world!\n', interval=secs_between_keys)
# Type with quarter-second pause in between each key
pyautogui.write('Hello world!', interval=0.25)

# Press the Esc key
pyautogui.press('esc')

# Hold the Shift key down and press the left arrow key 4 times
with pyautogui.hold('shift'):
    pyautogui.press(['left', 'left', 'left', 'left'])

# Press the Ctrl-C hotkey combination
pyautogui.hotkey('ctrl', 'c')

#################################################################
#                         Message Box                           #
#################################################################

# Make an alert box appear and pause the program until OK is clicked
pyautogui.alert('This is the message to display.')
pyautogui.confirm('This displays text and has an OK and Cancel button.')
pyautogui.prompt('This lets the user type in a string and press OK.')

# drags the mouse in a square spiral shape in MS Paint (or any graphics drawing program)
distance = 200
while distance > 0:
    pyautogui.drag(distance, 0, duration=0.5)   # move right
    distance -= 5
    pyautogui.drag(0, distance, duration=0.5)   # move down
    pyautogui.drag(-distance, 0, duration=0.5)  # move left
    distance -= 5
    pyautogui.drag(0, -distance, duration=0.5)  # move up

#################################################################
#                         Screenshot                            #
#################################################################
# returns a Pillow/PIL Image object
pyautogui.screenshot() # <PIL.Image.Image image mode=RGB size=1920x1080 at 0x24C3EF0>
# returns a Pillow/PIL Image object, and saves it to a file
pyautogui.screenshot('foo.png') # <PIL.Image.Image image mode=RGB size=1920x1080 at 0x31AA198>

# If you have an image file of something you want to click on, you can find it on the screen with
pyautogui.locateOnScreen('looksLikeThis.png')  # returns (left, top, width, height) of first place it is found
# (863, 417, 70, 13)
for i in pyautogui.locateAllOnScreen('looksLikeThis.png')
    ...
    ...
    # (863, 117, 70, 13)
    # (623, 137, 70, 13)
    # (853, 577, 70, 13)
    # (883, 617, 70, 13)
    # (973, 657, 70, 13)
    # (933, 877, 70, 13)

list(pyautogui.locateAllOnScreen('looksLikeThis.png'))
# [(863, 117, 70, 13), (623, 137, 70, 13), (853, 577, 70, 13), (883, 617, 70, 13), (973, 657, 70, 13), (933, 877, 70, 13)]



