#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import time

PI = 3.1415926535897

def circle():
 while(True):
    vel_msg.linear.x=0.2
    vel_msg.linear.y=0
    vel_msg.linear.z=0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0.2
    velocity_publisher.publish(vel_msg)


def rotate():

    speed = 10
    angle = 200

   
    angular_speed = speed*2*PI/360
    relative_angle = angle*2*PI/360

    vel_msg.linear.x=0
    vel_msg.linear.y=0
    vel_msg.linear.z=0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0

    
    vel_msg.angular.z = abs(angular_speed)
 
    t0 = rospy.Time.now().to_sec()
    current_angle = 0

    while(current_angle < relative_angle):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = angular_speed*(t1-t0)


    #Forcing our robot to stop
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)
    time.sleep(2)

def move(distance):
    #Receiveing the user's input
    speed = 10

    #Checking if the movement is forward or backwards
    #Since we are moving just in x-axis
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    vel_msg.linear.x = abs(speed)


        #Setting the current time for distance calculus
    t0 = rospy.Time.now().to_sec()
    current_distance = 0

        #Loop to move the turtle in an specified distance
    while(current_distance < distance):
            #Publish the velocity
        velocity_publisher.publish(vel_msg)
            #Takes actual time to velocity calculus
        t1=rospy.Time.now().to_sec()
            #Calculates distancePoseStamped
        current_distance= speed*(t1-t0)
        #After the loop, stops the robot
    vel_msg.linear.x = 0
    velocity_publisher.publish(vel_msg)
    time.sleep(2)

def stop():

    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    vel_msg.linear.x = 0

    velocity_publisher.publish(vel_msg)
           
if __name__ == '__main__':
 
        rospy.init_node('robot_cleaner', anonymous=True)
        velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        vel_msg = Twist()
    	#circle()
        move(distance=500)
        rotate()
        move(distance=50)
        rotate()
        move(distance=50)
        rotate()
        move(distance=50)
	stop()
   
