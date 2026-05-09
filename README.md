# MobileBot ROS2 Simulation

A 4-wheel differential drive mobile robot designed in Fusion 360 and simulated in ROS2 Humble and Gazebo Harmonic.

---

## Screenshots

### Gazebo and RViz
![simulation](images/simulation.png)

### Robot in RViz
![rviz](images/rviz.png)

### Robot in Gazebo
![gazebo](images/gazebo.png)

---

## Robot Description
- **Type**: 4-wheel differential drive
- **Design Tool**: Fusion 360
- **Wheel Separation**: 0.27m
- **Wheel Radius**: 0.04m
- **Total Mass**: ~4.4 kg
- **Simulator**: Gazebo Harmonic
- **Framework**: ROS2 Humble

---

## Package Structure
mobilebot/
├── urdf/           # Robot URDF and Xacro files
├── meshes/         # STL mesh files from Fusion 360
├── launch/         # ROS2 launch files
├── config/         # RViz configuration
├── scripts/        # Keyboard control scripts
├── images/         # Screenshots
└── CAD/            # Fusion 360 design files

---

## Requirements
- Ubuntu 22.04
- ROS2 Humble
- Gazebo Harmonic
- Python 3

---

## Installation
```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
git clone https://github.com/robo-afaq/mobilebot-R2.git mobilebot
cd ~/ros2_ws
colcon build --packages-select mobilebot_description
source install/setup.bash
```

---

## How to Run

### Terminal 1 — Launch Gazebo
```bash
source /opt/ros/humble/setup.bash
source ~/ros2_ws/install/setup.bash
ros2 launch mobilebot_description gazebo.launch.py
```

### Terminal 2 — Start Relay
```bash
source /opt/ros/humble/setup.bash
source ~/ros2_ws/install/setup.bash
python3 scripts/gz_relay.py
```

### Terminal 3 — Launch RViz
```bash
source /opt/ros/humble/setup.bash
source ~/ros2_ws/install/setup.bash
ros2 launch mobilebot_description display.launch.py
```

### Terminal 4 — Keyboard Control
```bash
source /opt/ros/humble/setup.bash
source ~/ros2_ws/install/setup.bash
python3 scripts/keyboard_control.py
```

---

## Controls
| Key | Action |
|-----|--------|
| w | Forward |
| s | Backward |
| a | Turn Left |
| d | Turn Right |
| x | Stop |
| q | Quit |

---

## Author
Muhammad Afaq

## License
MIT
