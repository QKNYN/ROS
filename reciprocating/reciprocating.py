#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1) #<1>
rospy.init_node('red_light_green_light')

turtle_move_twist = Twist() #<2>
turtle_front_twist = Twist()
turtle_front_twist.linear.x =  0.5 #<3>
turtle_back_twist = Twist()
turtle_back_twist.linear.x = -0.5 #<3>

driving_move = False
driving_front = True
driving_back = False
light_change_time = rospy.Time.now()
rate = rospy.Rate(10)

while not rospy.is_shutdown():
  if driving_move:
    if driving_back :
	cmd_vel_pub.publish(turtle_back_twist) #<4>
    if driving_front :
        cmd_vel_pub.publish(turtle_front_twist) #<4>        
  else:
    cmd_vel_pub.publish(turtle_move_twist)
  # BEGIN PART_1
  if rospy.Time.now() > light_change_time: #<5>
    driving_move = not driving_move
    if driving_move :
	driving_front = not driving_front
	driving_back  = not driving_back 
    light_change_time = rospy.Time.now() + rospy.Duration(3)
  # END PART_1
  rate.sleep() #<6>
