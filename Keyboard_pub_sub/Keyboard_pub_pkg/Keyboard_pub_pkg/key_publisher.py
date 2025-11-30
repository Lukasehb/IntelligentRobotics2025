import sys, termios, tty
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

def get_key():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    tty.setraw(fd)
    k = sys.stdin.read(1)
    termios.tcsetattr(fd, termios.TCSADRAIN, old)
    return k

class KeyPublisher(Node):
    def __init__(self):
        super().__init__('key_publisher')
        self.pub = self.create_publisher(String, '/robot_key', 10)

    def loop(self):
        while True:
            k = get_key()
            if k in ['z','s','a','e','x','q']:
                self.pub.publish(String(data=k))
            if k == 'q':
                break

def main():
    rclpy.init()
    n = KeyPublisher()
    n.loop()
    n.destroy_node()
    rclpy.shutdown()
