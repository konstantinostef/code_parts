import pyautogui
import time
    
def automate_task(numbers, seconds):
    
    # Wait for x seconds
    time.sleep(seconds)
    # Move the mouse to a specific position
    pyautogui.moveTo(1049, 557, duration=1) # Move inside PIN area
    # Click at the current mouse position
    pyautogui.click()
    # Loop through the numbers and press each one
    for number in numbers:
        pyautogui.press(number)

    # Move to OK
    pyautogui.moveTo(1057, 637)
    # Press OK
    pyautogui.click()
    # Move to OK for Wrong Password
    pyautogui.moveTo(1033, 590, duration=1)
    # Click OK for wrong password
    pyautogui.click()
    

# List of numbers to press
numbers = ['3', '7', '8', '8', '0', '9']
# Press Start Process
pyautogui.moveTo(1049, 730, duration=1) # Moves to (100, 100) in 1 second
# Click at the current mouse position
pyautogui.click()
seconds = 2 #Ξεκίνα με 3 δευτερόλεπτα και κάθε 200 έντυπα αύξανε τα δευτερόλεπτα αναμονής κατά 1

for k in range(1):
    seconds+=1
    for i in range(85):
        automate_task(numbers, seconds)

