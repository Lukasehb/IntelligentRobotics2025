import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial
import time

class VelocitySubscriber(Node):
    def __init__(self):
        super().__init__('velocity_subscriber')
        
        # Huidige snelheid bijhouden (state)
        self.left_speed = 0
        self.right_speed = 0

        try:
            self.ser = serial.Serial('/dev/ttyACM0', 57600, timeout=0.1)
            time.sleep(2) 
            self.get_logger().info("Verbonden met robot op /dev/ttyACM0")
        except Exception as e:
            self.get_logger().error(f"Kan seriële poort niet openen: {e}")
            self.ser = None

        self.create_subscription(String, '/robot_key', self.key_callback, 10)

    def send_command(self):
        if self.ser:
            # Maak het V-commando: V <Links> <Rechts>
            # Voorbeeld: "V 50 50"
            cmd = f"V {self.left_speed} {self.right_speed}"
            self.ser.write((cmd + "\n").encode())
            self.get_logger().info(f"Verzonden: {cmd}")

    def key_callback(self, msg):
        key = msg.data
        
        # Logica volgens jouw opdracht
        if key == 'z':
            # Snelheid + 5 (vooruit versnellen)
            self.left_speed += 5
            self.right_speed += 5
            
        elif key == 's':
            # Snelheid - 5 (trager of achteruit)
            self.left_speed -= 5
            self.right_speed -= 5
            
        elif key == 'a':
            # 1e wiel (links) +5, andere (rechts) -5 -> Draaibeweging
            self.left_speed += 5
            self.right_speed -= 5
            
        elif key == 'x':
            # Direct stoppen
            self.left_speed = 0
            self.right_speed = 0

        # Optioneel: Ik heb 'e' toegevoegd als logische tegenhanger van 'a'
        elif key == 'e':
            self.left_speed -= 5
            self.right_speed += 5

        # Stuur het nieuwe commando direct naar de robot
        self.send_command()

def main():
    rclpy.init()
    node = VelocitySubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        # Veiligheid: stop de robot bij afsluiten
        if node.ser:
            node.ser.write(b"V 0 0\n")
        node.destroy_node()
        rclpy.shutdown()
