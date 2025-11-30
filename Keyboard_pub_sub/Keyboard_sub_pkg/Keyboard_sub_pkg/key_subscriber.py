import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial
import time

KEYMAP = {
    'z': "D 50 50 1",   # forward
    's': "D -50 -50 1", # backward
    'a': "D 50 -50 1",  # left
    'e': "D -50 50 1",  # right
    'x': "D 0 0 1",     # stop
}

class KeySubscriber(Node):
    def __init__(self):
        super().__init__('key_subscriber')

        # Open the serial port to the robot
        try:
            self.ser = serial.Serial('/dev/ttyACM0', 57600, timeout=0.1)
            time.sleep(2)  # wait for the robot to be ready
        except Exception as e:
            self.get_logger().error(f"Cannot open serial port: {e}")
            self.ser = None

        # Subscribe to the key topic from the publisher
        self.create_subscription(String, '/robot_key', self.key_callback, 10)

    def key_callback(self, msg):
        key = msg.data
        command = KEYMAP.get(key)
        if command and self.ser:
            # Send the command to the robot
            self.ser.write((command + "\n").encode())
            self.get_logger().info(f"Sent command: {command}")

def main():
    rclpy.init()
    node = KeySubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
