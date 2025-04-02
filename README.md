# BuggyRobot-RaspberryProject 🤖

This project is a Raspberry Pi-controlled buggy robot powered by the `gpiozero` library. The robot can move in all directions—forward, backward, left, and right—with adjustable speed. It is controlled via a keyboard interface using the `curses` module for smooth operation.

## Features 🚀
- **Movement Control:** Forward, backward, left, and right
- **Adjustable Speed:** Low, Medium, High 🌟
- **Status Logging:** Logs robot status in `status.txt` 📝
- **Graceful Shutdown:** Shutdown Raspberry Pi safely 📴

## Hardware Requirements 🔧
- **Raspberry Pi** (Tested on Pi 5) 🖥️
- **L298N Motor Driver** 🔋
- **2 DC Motors** ⚙️
- **Power Source:** 12V battery recommended 🔋
- **Male-to-female jumper wires** 🔌

## Wiring Diagram 🧩

| **Motor Driver Pin** | **Raspberry Pi GPIO** |
|----------------------|-----------------------|
| IN1                  | GPIO 22 (Pin 15)      |
| IN2                  | GPIO 17 (Pin 11)      |
| IN3                  | GPIO 23 (Pin 16)      |
| IN4                  | GPIO 24 (Pin 18)      |
| ENA                  | Connected to 3.3V or PWM control |
| ENB                  | Connected to 3.3V or PWM control |

## Installation 🛠️

1. **Install Dependencies:**

    ```bash
    sudo apt update
    sudo apt install python3-gpiozero
    ```

2. **Clone the Repository:**

    ```bash
    git clone https://github.com/Samuel-Gbadamosi/BuggyRobot-RaspBerryProject.git
    cd BuggyRobot
    ```

3. **Run the Robot Script:**

    ```bash
    python3 robot.py
    ```

## Controls 🎮

| **Key**         | **Action**        |
|-----------------|-------------------|
| ↑ (UP Arrow)    | Move Forward      |
| ↓ (DOWN Arrow)  | Move Backward     |
| ← (LEFT Arrow)  | Turn Left         |
| → (RIGHT Arrow) | Turn Right        |
| 'l'             | Set speed to Low  |
| 'm'             | Set speed to Medium |
| 'h'             | Set speed to High |
| 'p'             | Shutdown Raspberry Pi |
| 'q'             | Quit the program  |

## Status Logging 📝

The robot's current status (movement direction and speed) is logged in `status.txt` for future reference and debugging.

## Troubleshooting ⚠️

### **Motors Not Moving?**
- Check wiring connections.
- Ensure the motor driver is powered properly.
- Run `gpioset` commands to test individual GPIO states.

### **Only One Motor Works?**
- Swap motor connections to confirm if the issue is wiring-related.
- Ensure both ENA and ENB are powered or controlled via PWM.

### **No Key Presses Detected?**
- Run `robot.py` with `sudo`.
- Add `print(f"Key pressed: {char}")` in the loop to debug key inputs.

## Contributing 🤝

Feel free to fork the repository and submit pull requests for improvements! Contributions are always welcome 😎.

---

Enjoy building and controlling your BuggyRobot! 🚗💨

Created by Samuel Gbadamosi 

