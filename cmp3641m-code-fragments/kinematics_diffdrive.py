import math
from geometry_msgs.msg import Twist

wheel_radius = 1 / (math.pi * 2.0)
robot_radius = 1

wheel_circumference = 2 * math.pi * wheel_radius


# computing the forward kinematics for a differential drive
def forward_kinematics(w_l, w_r):
    c_l = wheel_circumference * w_l
    c_r = wheel_circumference * w_r
    v = (c_l + c_r) / 2
    a = (c_l - c_r) / robot_radius
    return (v, a)


# computing the inverse kinematics for a differential drive
def inverse_kinematics(v, a):
    c_l = v + (robot_radius * a) / 2
    c_r = v - (robot_radius * a) / 2
    w_l = c_l / wheel_circumference
    w_r = c_r / wheel_circumference
    return (w_l, w_r)


# inverse kinematics from a Twist message (This is what a ROS robot has to do)
def inverse_kinematics_from_twist(t):
    return inverse_kinematics(t.linear.x, t.angular.z)


(w_l, w_r) = inverse_kinematics(0.0, 2 * math.pi)
print "w_l = %f,\tw_r = %f" % (w_l, w_r)

(v, a) = forward_kinematics(w_l, w_r)
print "v = %f,\ta = %f" % (v, a)

t = Twist()

t.linear.x = 0.0
t.angular.z = math.pi

(w_l, w_r) = inverse_kinematics_from_twist(t)
print "w_l = %f,\tw_r = %f" % (w_l, w_r)
