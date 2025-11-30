# Import the ROS 2 Python client library
import rclpy

# Import the Node base class to define a ROS 2 node
from rclpy.node import Node

# Import the standard ROS 2 message type 'Float32'
from std_msgs.msg import Float32
import random

# Define a class that represents our node (inherits from Node)
class BatteryVoltagePublisher(Node):
    def __init__(self):
        super().__init__('battery_voltage')
        # Create a publisher that sends String messages on the 'chatter_pkg' topic
        self.pub = self.create_publisher(Float32, '/battery_voltage', 10)
        # Create a timer that calls the tick() method every 0.5 seconds
        self.timer = self.create_timer(60.0, self.publish_voltage)

    def publish_voltage(self):
        voltage = 11.0 + random.random() * 2.0
        msg = Float32()
        msg.data = voltage
        self.pub.publish(msg)



def main():
    rclpy.init()
    node = BatteryVoltagePublisher()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
