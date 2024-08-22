#USED CHATGPT#
import pyautogui
import time

# Create a combined list of all characters
keys_lower = list("abcdefghijklmnopqrstuvwxyz .,'?")

# Add a message for the user
print("The script will start in 5 seconds. Move your mouse to the top-left corner of the screen or press 'Ctrl+C' to stop the script.")

# Give yourself time to switch to the application where you want to simulate key presses
time.sleep(5)

# Enable pyautogui's fail-safe feature (moving the mouse to the top-left corner stops the script)
pyautogui.FAILSAFE = True

# Loop infinitely, pressing all keys at once in quick succession
try:
    while True:
        # Press all lowercase keys
        pyautogui.hotkey(*keys_lower)

except pyautogui.FailSafeException:
    print("Mouse moved to the top-left corner. Script terminated.")
except KeyboardInterrupt:
    print("Script terminated by user.")
