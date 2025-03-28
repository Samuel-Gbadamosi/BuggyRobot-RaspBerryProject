from gpiozero import Robot
from time import sleep
import os
import curses

robby = Robot(left=(22,17), right=(23,24))
print('robby initialized')

# Default speed and status
speed = 0.6
status = "Idle"

def update_status():
    with open("status.txt", "w") as f:
        f.write(f"Status: {status}\nSpeed: {speed:.1f}")

screen = curses.initscr()
curses.noecho()
curses.cbreak()
curses.halfdelay(3)
screen.keypad(True)

try:
    while True:
        char = screen.getch()

        if char == ord('q'):
            break
        elif char == ord('p'):
            curses.nocbreak()
            screen.keypad(0)
            curses.echo()
            curses.endwin()
            os.system('sudo halt')
        
        elif char == curses.KEY_UP:
            robby.forward(speed)
            status = "Moving Forward"
            print(f'Forward at speed {speed}')
        
        elif char == curses.KEY_DOWN:
            robby.backward(speed)
            status = "Moving Backward"
            print(f'Backward at speed {speed}')
        
        elif char == curses.KEY_LEFT:
            robby.left(speed)
            status = "Turning Left"
            print(f'Left at speed {speed}')
        
        elif char == curses.KEY_RIGHT:
            robby.right(speed)
            status = "Turning Right"
            print(f'Right at speed {speed}')
        
        elif char == ord('l'):  
            speed = 0.4
            status = "Speed set to LOW"
            print("Speed set to LOW (0.4)")
        
        elif char == ord('m'):  
            speed = 0.6
            status = "Speed set to MEDIUM"
            print("Speed set to MEDIUM (0.6)")
        
        elif char == ord('h'):  
            speed = 0.9
            status = "Speed set to HIGH"
            print("Speed set to HIGH (0.9)")

        else:
            robby.stop()
            if status not in ["Stopped", "Idle"]:  # Only update if changing from movement
                status = "Stopped"
                print("Stopped")

        update_status()  # Only update when something changes

finally:
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()