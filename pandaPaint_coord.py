#!/usr/bin/env python
#ROS specific

def paint(word, y_coord, frameScale):
	import sys
	import copy
	import rospy
	import moveit_commander
	import geometry_msgs.msg
	from std_msgs.msg import Float64MultiArray, MultiArrayDimension

	from math import pi
	import tf


	import test_han_all
	framelist = test_han_all.get_coordinates(word, frameScale)

	#The X,Y,Z coordinates of the centre of the drawing space (M)
	oOffCords = [0.58,y_coord,0.2028]
	# oOffCords = [0.58,y_coord,0.2035] #DATE0706
	# oOffCords = [0.58,y_coord,0.2045] #DATE0622

	#The pitch, roll yaw andgles of the end effector when drawing (radians)
	oOffRots = [pi,0,-pi/4]

	#Set the time required (s)
	processingTime = 0.3


	#This function takes a frame of coordinates and executes the drawing of the frame
	def goOnPath(frame):
		#Clear previous pose targets
		group.clear_pose_targets()

		#Create an empty list to store the frame coordinates
		drawpoints = []

		for coordinate in frame:
			
			#Calculate the quaternion of the end effector facing forward
			quaternion = tf.transformations.quaternion_from_euler(oOffRots[0],oOffRots[1],oOffRots[2])

			#Initialise the drawpose message 
			drawpose = geometry_msgs.msg.Pose()

			#update the drawpose message base upon the required rotation and coordinate location of the end effector
			drawpose.orientation.x = quaternion[0]
			drawpose.orientation.y = quaternion[1]
			drawpose.orientation.z = quaternion[2]
			drawpose.orientation.w = quaternion[3]
			drawpose.position.x = oOffCords[0] + coordinate[0] *frameScale
			drawpose.position.y = oOffCords[1] + coordinate[1] *frameScale
			# drawpose.position.z = oOffCords[2] + coordinate[2]
			drawpose.position.z = oOffCords[2] + coordinate[2] *frameScale

			# print("HERE IS COORDINATE IN FRAME:")
			# print(drawpose)

			#Add the drawpose message to the list of drawpoints
			drawpoints.append(copy.deepcopy(drawpose))

		#Calculate motion path base on drawpoints list
		(plan, fraction) = group.compute_cartesian_path(drawpoints, 0.01, 0.0)

		#Execute the calculated motion plan and wait until complete
		group.execute(plan, wait=True) 



	#Main code exeution by Panda

	#Create rospy node
	rospy.init_node('panda_paint_controller', anonymous=True)

	#Initialise motion planning in RVIZ
	moveit_commander.roscpp_initialize(sys.argv)	
	robot = moveit_commander.RobotCommander()
	scene = moveit_commander.PlanningSceneInterface()
	group_name = "panda_arm"
	group = moveit_commander.MoveGroupCommander(group_name)



	#Iterate through each frame in the framlist of the whole animation
	for frame in framelist:

		#start
		print("Start!")

		#Wait 1 second
		rospy.sleep(processingTime)

		#Execute frame motion
		goOnPath(frame)

		#User inform message
		print("Done!")

		#Wait time before next frame
		rospy.sleep(processingTime)