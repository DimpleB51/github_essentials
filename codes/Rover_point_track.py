#! /usr/bin/env python3

import numpy as np
# from motors import Rover
# from fusion import states
# from imu import heading_angle
from iq_gnc.py_gnc_functions import *
from iq_gnc.PrintColours import *
from feedback_loop import *
from math import sqrt, atan2, pi, copysign, cos, sin
from time import sleep
import rospy
import csv
from geometry_msgs.msg import Twist
from iq_gnc.py_gnc_functions import *
# To print colours (optional).
from iq_gnc.PrintColours import *


def wrap_2_180(value):
    if value > 180:
        value -= 360
    elif value < -180:
        value += 360

    return value


class Point_Tracking:

    def __init__(self):
        self.pose = None
        # rospy.init_node('pose_listener')
        self.drone = gnc_api()
        # Wait for FCU connection.
        self.drone.wait4connect()
        self.poseListener = PoseListener()  # Replace 'your_pose_topic'
        #set_mode_client = rospy.ServiceProxy("/mavros/set_mode", SetMode)
        self.pub_vel = rospy.Publisher('/mavros/setpoint_velocity/cmd_vel_unstamped', Twist, queue_size=10)

        sleep(0.5)
        self.init_pose = self.drone.get_current_heading()
        self.frame_yaw = self.init_pose[2] * pi / 180
        #self.rot_mat = np.array([[cos(self.frame_yaw), sin(self.frame_yaw)], [-sin(self.frame_yaw), cos(self.frame_yaw)]])
        print(f"Initial state: ", self.init_pose)
        self.rate = rospy.Rate(10)
        # self.my_rover = Rover()
        self.states = []

    def goal_WF(self, goal_LF):
        
        self.rot_mat = np.array([[cos(self.frame_yaw), -sin(self.frame_yaw)], [sin(self.frame_yaw), cos(self.frame_yaw)]])
        goal_wf = self.pose[0:2] + np.matmul(self.rot_mat, goal_LF)

        return goal_wf


    def euclidean_distance(self, goal):
        return sqrt((goal[0] - self.pose[0]) ** 2 + (goal[1] - self.pose[1]) ** 2)

    def angular_distance(self, goal):
        return atan2((goal[1] - self.pose[1]), (goal[0] - self.pose[0]))

    def export_data(self, file_name):

        fields = ["x", "y", "theta"]

        with open(file_name, 'w') as f:
            # using csv.writer method from CSV package
            write = csv.writer(f)

            write.writerow(fields)
            write.writerows(self.states)

    # def final_heading(self, fin_head_angle):

    #     self.pose = self.poseListener.get_pose()
    #     self.pose[2] = round(wrap_2_180(self.pose[2]) * pi / 180, 3)
    #     my_heading = self.pose[2]

    #     while abs(my_heading - fin_head_angle) >= 0.2:

    #         sign = (fin_head_angle - my_heading) / abs(my_heading - fin_head_angle)
    #         self.my_rover.cmd_ang_vel(0.7 * sign)
    #         sleep(0.15)
    #         self.my_rover.cmd_stop()
    #         sleep(0.05)

    #         self.pose = self.poseListener.get_pose()
    #         self.pose[2] = round(wrap_2_180(self.pose[2] - self.init_pose[2]) * pi / 180, 3)
    #         my_heading = self.pose[2]

    #     self.my_rover.cmd_stop()
    #     return

    def run(self, goal_point, final_heading_angle=0, file_name="states_1.csv"):
        rate = rospy.Rate(3)
        #sleep(1.5)
        self.init_pose = self.drone.get_current_heading()
        while not rospy.is_shutdown():
        
            self.pose = self.drone.get_current_heading()
            rate = rospy.Rate(3)
            #goal_point = self.goal_WF(goal_point)   # Goal point in world frame
            #self.pose[0:2] = self.rot_mat @ self.pose[0:2]
            #self.pose[0] = round(self.pose[0] - self.init_pose[0], 2)
            #self.pose[1] = round(self.pose[1] - self.init_pose[1], 2)
            #self.pose[2] = round(wrap_2_180(self.pose[2] - self.init_pose[2]) * pi / 180, 3)
            self.pose[2] = round(wrap_2_180(self.pose[2]) * pi / 180, 3)
            
            print(f"my states: {self.pose}")
            self.states.append([self.pose[0], self.pose[1], self.pose[2]])

            ang_error = round(self.angular_distance(goal_point) - self.pose[2], 3)
            lin_error = self.euclidean_distance(goal_point)
            # print("Angular error",ang_error)
            pub = Twist()
            print(ang_error, lin_error)
            if abs(ang_error) >= 0.15:
                print("Angular error",ang_error)
                # self.my_rover.cmd_ang_vel(0.02 * (ang_error / abs(ang_error)))
                pub.linear.x = 0
                pub.linear.y = 0
                pub.angular.z = 0.1 * copysign(1,ang_error)
                pub.linear.z = 0
                self.pub_vel.publish(pub)
                # sleep(0.15)
                # pub.linear.x = 0
                # pub.linear.y = 0
                # pub.angular.z = 0
                # self.pub_vel(pub)
                # sleep(0.05)

            elif lin_error >= 0.5:
                # self.my_rover.cmd_lin_vel(0.4)
                v_lin = 0.6
                pub.linear.x = v_lin * cos(self.pose[2])
                pub.linear.y = v_lin * sin(self.pose[2])
                pub.angular.z = 0
                pub.linear.z = 0
                self.pub_vel.publish(pub)

            elif ang_error < 0.2 and lin_error < 0.5:
                # self.my_rover.cmd_stop()
                pub.linear.x = 0
                pub.linear.y = 0
                pub.angular.z = 0
                self.pub_vel.publish(pub)
                self.drone.land()
                print("Reached the goal...")
                #self.final_heading(final_heading_angle)
                #print("Reached the final heading...")
                sleep(2)
                break
        self.export_data(file_name)
        rate.sleep()

if __name__ == '__main__':

    my_PT = Point_Tracking()
    goal = np.array([0.6, 0.6])
    final_head = 0

    my_PT.run(goal, final_head, "my_states_7.csv")

