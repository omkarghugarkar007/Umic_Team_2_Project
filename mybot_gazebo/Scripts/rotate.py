#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion, quaternion_from_euler
from geometry_msgs.msg import Twist
import math

def move(distance):
    #Receiveing the user's input
    speed = 1
    print("In Move")

    #Checking if the movement is forward or backwards
    #Since we are moving just in x-axis
    command.linear.y = 0
    command.linear.z = 0
    command.angular.x = 0
    command.angular.y = 0
    command.angular.z = 0

    command.linear.x = abs(speed)


        #Setting the current time for distance calculus
    t0 = rospy.Time.now().to_sec()
    current_distance = 0

        #Loop to move the turtle in an specified distance
    while(current_distance < distance):
            #Publish the velocity
        pub.publish(command)
	#print("Done")
            #Takes actual time to velocity calculus
        t1=rospy.Time.now().to_sec()
            #Calculates distancePoseStamped
        current_distance= speed*(t1-t0)
        #After the loop, stops the robot
    
    command.linear.x = 0
    pub.publish(command)
    

def stop():

    command.linear.y = 0
    command.linear.z = 0
    command.angular.x = 0
    command.angular.y = 0
    command.angular.z = 0

    command.linear.x = 0

    pub.publish(command)
           
def get_rotation(msg):

	global roll,pitch,yaw
	orientation_q = msg.pose.pose.orientation
	orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]

	(roll,pitch,yaw) = euler_from_quaternion(orientation_list)
	#print(yaw)


def rotate(target):
 
	# range of target -180 to 180
	while not rospy.is_shutdown():
		
		command.linear.y = 0
		command.linear.z = 0
		command.angular.x = 0
		command.angular.y = 0
		command.linear.x = 0
		
		target_rad = target*math.pi/180
		diff = target_rad-yaw 
		command.angular.z =kP*diff
		pub.publish(command)
		if diff <0.05:
			print("Rotation Complete")
			command.angular.z = 0
			pub.publish(command)
			return
		#print("Target={} Current={}".format(target_rad,yaw))

		r.sleep()

if __name__ == '__main__':

	kP = 5

	roll=0.0
	pitch=0.0
	yaw=0.0

	rospy.init_node('rotate_robot')
	sub = rospy.Subscriber('/odom',Odometry,get_rotation)
	pub = rospy.Publisher('/cmd_vel', Twist,queue_size = 1)
	r = rospy.Rate(10)
	command = Twist()

	print("1")
	rotate(target =0)
	print("2")
	move(distance=2)
	print("3")
	stop()
	rotate(target=90)
	print("4")
	stop()
	move(distance=30)
	print("5")
	stop()
	rotate(target=180)
	print("5")
	stop()
	move(distance=20)
	print("6")
	rotate(target=-90)
	print("7")
	move(distance=30)

	


