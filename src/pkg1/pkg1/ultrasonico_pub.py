import rclpy
from rclpy.node import Node
import random 
#Cambiar el tipo de mensaje a Int32 (o Float32 si prefieres decimales)
from std_msgs.msg import Int32 

class UltrasonicPublisher(Node):

    def __init__(self):
        super().__init__('Ultrasonico_Publisher')
        self.publisher_ = self.create_publisher(Int32, 'Distancia', 10)
        timer_period = 0.5  # segundos
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Int32()
        # 4. Generar un número aleatorio (ejemplo: entre 0 y 100)
        msg.data = random.randint(0, 400) 
        
        self.publisher_.publish(msg)
        self.get_logger().info('Publicando Distancia: "%d"' % msg.data)


def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = UltrasonicPublisher()
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()