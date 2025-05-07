import rclpy
from rclpy.node import Node
from visualization_msgs.msg import Marker
import sys

class publishedMarkerValue(Node):
    def __init__(self, xPosition, yPosition, degreesValue):
        super().__init__('goal_marker_publisher')
        generatedPublisher = self.create_publisher(Marker, '/goal_marker', 10)

        generatedMarkerValue = Marker()
        generatedMarkerValue.header.frame_id = "map"
        generatedMarkerValue.type = Marker.SPHERE
        generatedMarkerValue.action = Marker.ADD
        generatedMarkerValue.pose.position.x = float(xPosition)
        generatedMarkerValue.pose.position.y = float(yPosition)
        generatedMarkerValue.pose.position.z = 0.1
        generatedMarkerValue.pose.orientation.w = 1.0
        generatedMarkerValue.scale.x = 0.3
        generatedMarkerValue.scale.y = 0.3
        generatedMarkerValue.scale.z = 0.3
        generatedMarkerValue.color.a = 1.0
        generatedMarkerValue.color.r = 0.9
        generatedMarkerValue.color.g = 0.1
        generatedMarkerValue.color.b = 0.1
