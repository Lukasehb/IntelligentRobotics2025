import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class BatterySubscriber(Node):
    def __init__(self):
        super().__init__('battery_subscriber')
        self.sub = self.create_subscription(Float32, '/battery_voltage', self.callback, 10)

    def callback(self, msg):
        voltage = msg.data
        if voltage < 11.5:
            print(f"WARNING: low voltage: {voltage} V")

def main():
    rclpy.init()
    node = BatterySubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
