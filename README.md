# 🤖 BuggyRobot-RaspBerryProject

This project is a Raspberry Pi-controlled buggy robot using the gpiozero library. The robot can move forward, backward, left, and right, with adjustable speed, and is controlled via a keyboard interface using the curses module.

Features

Forward, backward, left, and right movement

Adjustable speed (Low, Medium, High)

Status logging to status.txt

Graceful shutdown command

Hardware Requirements

Raspberry Pi (tested on Pi 5)

L298N Motor Driver

2 DC motors

Power source (12V battery recommended)

Male-to-female jumper wires

Wiring Diagram

Motor Driver Pin

Raspberry Pi GPIO

IN1

GPIO 22 (Pin 15)

IN2

GPIO 17 (Pin 11)

IN3

GPIO 23 (Pin 16)

IN4

GPIO 24 (Pin 18)

ENA

Connected to 3.3V or PWM control

ENB

Connected to 3.3V or PWM control

Installation

Install Dependencies:

sudo apt update
sudo apt install python3-gpiozero

Clone the Repository:

git clone https://github.com/Samuel-Gbadamosi/BuggyRobot-RaspBerryProject.git


cd BuggyRobot

Run the Robot Script:

python3 robot.py

Controls

Key

Action

UP Arrow

Move Forward

DOWN Arrow

Move Backward

LEFT Arrow

Turn Left

RIGHT Arrow

Turn Right

'l'

Set speed to Low

'm'

Set speed to Medium

'h'

Set speed to High

'p'

Shutdown Raspberry Pi

'q'

Quit the program

Status Logging

The robot's current status (movement direction and speed) is logged in status.txt.

Troubleshooting

Motors Not Moving?

Check wiring connections.

Ensure motor driver is powered properly.

Run gpioset commands to test individual GPIO states.

Only One Motor Works?

Swap motor connections to confirm if the issue is wiring-related.

Ensure both ENA and ENB are powered or controlled via PWM.

No Key Presses Detected?

Run robot.py with sudo.

Add print(f"Key pressed: {char}") in the loop to debug key inputs.

Contributing

Feel free to fork the repository and submit pull requests for improvements!

License

This project is open-source under the MIT License.
