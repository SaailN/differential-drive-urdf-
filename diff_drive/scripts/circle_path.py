#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def talker():
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)   
    rospy.init_node('velocity_pub', anonymous=False)
    msg = Twist()
    msg.linear.x = 0
    msg.linear.y = 0.3
    msg.linear.z = 0
    msg.angular.x = 0
    msg.angular.y = 0
    msg.angular.z = 0
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass