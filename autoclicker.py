import pyautogui
from pynput.keyboard import Key, Listener

#  ======== settings ========
delay = 0.1  # in seconds
main_key = Key.f2
exit_key = Key.esc
#  ==========================

running = True
pause = True  # Initially set to True to wait for F2 to be pressed


def on_press(key):
    global running, pause

    if key == main_key:
        pause = not pause
        if pause:
            print("[Paused]")
        else:
            print("[Resumed]")
    elif key == exit_key:
        running = False
        print("[Exit]")


def get_delay():
    global delay
    delay = float(input("Enter the delay (in seconds): "))


def display_controls():
    print("// AutoClicker")
    print("// - Controls:")
    print("\t F2 = Resume/Pause")
    print("\t Esc = Exit")
    print("-----------------------------------------------------")
    print('Press F2 to start ...')


def main():
    global pause
    get_delay()
    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()

    while pause:  # Wait for F2 to be pressed
        pass

    # Now, start auto-clicking
    while running:
        if not pause:
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = delay

    lis.stop()


if __name__ == "__main__":
    main()

