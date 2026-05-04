import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import subprocess

class CmdVelRelay(Node):
    def __init__(self):
        super().__init__('cmd_vel_relay')
        self.sub = self.create_subscription(Twist, '/cmd_vel', self.callback, 10)
        self.get_logger().info('Relay started!')

    def callback(self, msg):
        cmd = 'gz topic -t /cmd_vel -m gz.msgs.Twist -p "linear: {x: ' + str(msg.linear.x) + '}, angular: {z: ' + str(msg.angular.z) + '}"'
        subprocess.Popen(cmd, shell=True)
        self.get_logger().info('Sent: linear=' + str(msg.linear.x) + ' angular=' + str(msg.angular.z))

def main():
    rclpy.init()
    node = CmdVelRelay()
    rclpy.spin(node)

main()
