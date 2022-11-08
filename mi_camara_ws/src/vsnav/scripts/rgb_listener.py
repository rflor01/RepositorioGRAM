#!/usr/bin/env python3

import rospy
import cv2
from rgb_reader import CameraListener


if __name__ == '__main__':

    c = CameraListener()

    # When doing init_node we will initialize the camera_node
    rospy.init_node("camera_listener", anonymous=True)

    while 1:
        if c.post_image() is not None:
            cv2.imshow("My_image", c.post_image())

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
