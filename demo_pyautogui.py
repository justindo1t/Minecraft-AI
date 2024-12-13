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

#################################################################
#                        Mouse Operation                        #
#################################################################

# Move the mouse to XY coordinates
pyautogui.moveTo(100, 150)

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

# Type with quarter-second pause in between each key
pyautogui.write('Hello world!', interval=0.25)

# Press the Esc key
pyautogui.press('esc')

# Hold the Shift key down and press the left arrow key 4 times
with pyautogui.hold('shift'):
    pyautogui.press(['left', 'left', 'left', 'left'])

# Press the Ctrl-C hotkey combination
pyautogui.hotkey('ctrl', 'c')

# Make an alert box appear and pause the program until OK is clicked
pyautogui.alert('This is the message to display.')

# drags the mouse in a square spiral shape in MS Paint (or any graphics drawing program)
distance = 200
while distance > 0:
    pyautogui.drag(distance, 0, duration=0.5)   # move right
    distance -= 5
    pyautogui.drag(0, distance, duration=0.5)   # move down
    pyautogui.drag(-distance, 0, duration=0.5)  # move left
    distance -= 5
    pyautogui.drag(0, -distance, duration=0.5)  # move up
