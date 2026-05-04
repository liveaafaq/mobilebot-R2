import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys
import tty
import termios

class KeyboardControl(Node):
    def __init__(self):
        super().__init__('keyboard_control')
        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.speed = 0.3
        self.turn = 0.5
        print("w=forward s=backward a=left d=right x=stop q=quit")

    def get_key(self):
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)

    def run(self):
        while True:
            key = self.get_key()
            msg = Twist()
            if key == 'w':
                msg.linear.x = self.speed
                print('Forward')
            elif key == 's':
                msg.linear.x = -self.speed
                print('Backward')
            elif key == 'a':
                msg.angular.z = -self.turn
                print('Left')
            elif key == 'd':
                msg.angular.z = self.turn
                print('Right')
            elif key == 'x':
                print('Stop')
            elif key == 'q':
                print('Quit')
                break
            self.pub.publish(msg)

def main():
    rclpy.init()
    node = KeyboardControl()
    node.run()
    rclpy.shutdown()

main()
