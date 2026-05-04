# MobileBot ROS2 Simulation

A 4-wheel differential drive mobile robot simulated in ROS2 Humble and Gazebo Harmonic.

## Features
- Designed in Fusion 360
- URDF/Xacro robot description
- Gazebo Harmonic simulation
- RViz visualization
- Keyboard control (w/a/s/d)

## Requirements
- Ubuntu 22.04
- ROS2 Humble
- Gazebo Harmonic

## Launch Gazebo
ros2 launch mobilebot_description gazebo.launch.py

## Launch RViz
ros2 launch mobilebot_description display.launch.py

## Keyboard Control
python3 scripts/keyboard_control.py
- w = forward
- s = backward
- a = turn left
- d = turn right
- x = stop
- q = quit
