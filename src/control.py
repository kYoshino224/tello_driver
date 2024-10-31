import numpy as np
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty

# Initialize the ROS node and publisher
rospy.init_node('manipulate_tello')
tello_takeoff = rospy.Publisher('/tello/takeoff', Empty, queue_size=1)
tello_cmd_vel = rospy.Publisher('/tello/cmd_vel', Twist, queue_size=1)
tello_land = rospy.Publisher('/tello/land', Empty, queue_size=1)
rate = rospy.Rate(10)

# Define movement commands
empty = Empty()
move_straight = Twist()
turn_left = Twist()
move_straight.linear.x = 0.5
turn_left.angular.z = np.pi/2

def main():
    count = -1
    while not rospy.is_shutdown():
        if count == -1:
            tello_takeoff.publish(empty)
        elif count >= 0 and count < 10:
            tello_cmd_vel.publish(move_straight)
        elif count == 10:
            tello_cmd_vel.publish(turn_left)
            count = 0
        else:
            tello_land.publish(empty)
            break               
        count += 1
    rate.sleep()
        

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
