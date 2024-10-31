#!/usr/bin/env python3

import numpy as np
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty

# Initialize the ROS node and publisher
rospy.init_node('manipulate_tello')
tello_takeoff = rospy.Publisher('/tello/takeoff', Empty, queue_size=1)
tello_cmd_vel = rospy.Publisher('/tello/cmd_vel', Twist, queue_size=1)
tello_land = rospy.Publisher('/tello/land', Empty, queue_size=1)

# Define movement commands
empty = Empty()
move_straight = Twist()
turn_left = Twist()
stop = Twist()
move_straight.linear.x = 0.2
turn_left.angular.z = np.pi/4

def main():
    count = -1
    while not rospy.is_shutdown():
        if count == -1:
            rospy.sleep(0.1)
            tello_takeoff.publish(empty)
            rospy.sleep(4)
            count += 1
        #elif count >= 0 and count < 10:
            #rospy.sleep(0.1)
            #tello_cmd_vel.publish(move_straight)
            #rospy.sleep(1)
            #tello_cmd_vel.publish(stop)
            #rospy.sleep(2)
        elif count <= 4 and count >= 0:
            rospy.sleep(0.1)
            tello_cmd_vel.publish(turn_left)
            rospy.sleep(2)
            tello_cmd_vel.publish(stop)
            rospy.sleep(2)
            count += 1
        else:
            rospy.sleep(0.1)
            tello_land.publish(empty)
            break               
        
        

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
