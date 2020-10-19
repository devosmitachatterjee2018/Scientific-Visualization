import bpy
from mathutils import *
from math import *

# Initial data
q = Quaternion((1,0,0,0))
omega = Vector((1e-2, 1, 0))

# Create quaternions
#q1 = Quaternion((1.0, 2.0, 3.0, 4.0))
#q2 = Quaternion((0.0, 0.5, 1.5, -0.5))
# Multiplication of quaternions
# q3 = q1*q2
# Quaternion((-3.5, -7.0, 4.5, 1.0))

# Variable for currently active object
myobj = bpy.data.objects['Sphere']
myobj.rotation_mode = 'QUATERNION'
#q = myobj.rotation_quaternion
# Quaternion((1.0, 0.0, 0.0, 0.0))

# omega1 = Vector((1.0, -3.0, 0.0))
# omega2 = Vector((0.0, 2.0, -2.0))
# omega3 = omega1.cross(omega2)
# Vector((6.0, 2.0, 2.0))

I = Matrix(((0.5,0,0),(0,2,0),(0,0,4)))
Inv_I = I.inverted()
# Matrix(((2.0, 0.0, 0.0), (0.0, 0.5, 0.0), (0.0, 0.0, 0.25)))

# I*omega
# Euler equations
# omegadot = -Inv_I*(omega.cross(I*omega))
# h = 0.01
# dq = Quaternion(h*omega)
# q = q*dq
# Quaternion((0.877570629119873, 0.004794234409928322, 0.4794234335422516, 0.0))

# Clear all previous animation data
myobj.animation_data_clear()

# set first and last frame index
total_time = 25 # Animation should be 25 seconds long
fps = 24 # Frames per second (fps)
bpy.context.scene.frame_start = 0
bpy.context.scene.frame_end = 250

h = 0.01
# loop of frames and insert keyframes every 10th frame
keyframe_freq = 10
nlast = 2500
for n in range(nlast):
    t = total_time*n/nlast
    # Do computations here...
    omega = omega - h*Inv_I*(omega.cross(I*omega))
    dq = Quaternion(h*omega)
    q = q*dq
    # Check if n is a multiple of keyframe_freq
    if n%keyframe_freq == 0:
        bpy.context.scene.frame_set(n//10)
        # Set current location like this
        myobj.rotation_quaternion = q
        # Insert new keyframe for "location" like this
        myobj.keyframe_insert(data_path="rotation_quaternion")