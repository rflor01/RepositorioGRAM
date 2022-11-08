import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


class CameraListener:
    def __init__(self):
        self.bridge = CvBridge()
        self.sub_name = "/camera/color/image_raw"
        self.rgb_image = None

        # When receiving a ROS image message we will execute the callback_rgb function
        # sending the data received (the image)
        rospy.Subscriber(self.sub_name, Image, self._callback_rgb)

    def post_image(self):
        return self.rgb_image

    def _callback_rgb(self, data):
        try:
            # Saving the rgb image in rgb_image
            self.rgb_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
            # We will also save the ros_rgb_image at ros_rgb_image, i dont know why
            # self.ros_rgb_image = data

        except CvBridgeError as e:
            print(e)
