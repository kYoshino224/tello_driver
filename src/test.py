#!/usr/bin/env python3

import numpy as np
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty

if __name__ == '__main__':

    rospy.init_node('manipulate_tello')

    rospy.loginfo("test")

    tello_takeoff = rospy.Publisher('/tello/takeoff', Empty, queue_size=1)
    empty = Empty()

    rospy.sleep(0.1)
    tello_takeoff.publish(empty)
    # rospy.sleep(1)

