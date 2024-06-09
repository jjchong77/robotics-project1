#!/usr/bin/env python3
"""code broadcasted message correctly, but was not accepted by gazebo?
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class RobotController(Node):

    def __init__(self):
        super().__init__('robot_controller')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 0.5
        msg.angular.z = 0.05
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: linear.x = %f, angular.z = %f' % (msg.linear.x, msg.angular.z))

def main(args=None):
    rclpy.init(args=args)
    robot_controller = RobotController()
    rclpy.spin(robot_controller)
    robot_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

"""
#!/usr/bin/env python3
#this version runs the following line on the command line
#gz topic -t "/cmd_vel" -m gz.msgs.Twist -p "linear: {x: 0.5}, angular: {z: 0.05}"
import rclpy
from rclpy.node import Node
import subprocess

class RobotController(Node):

    def __init__(self):
        super().__init__('robot_controller')
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        # Define the gz topic command
        cmd = [
            'gz', 'topic', '-t', '/cmd_vel',
            '-m', 'gz.msgs.Twist',
            '-p', 'linear: {x: 0.5}, angular: {z: 0.05}'
        ]
        # Run the command
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            self.get_logger().error(f'Command failed: {result.stderr}')
        else:
            self.get_logger().info('Command executed successfully.')

def main(args=None):
    rclpy.init(args=args)
    robot_controller = RobotController()
    rclpy.spin(robot_controller)
    robot_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
