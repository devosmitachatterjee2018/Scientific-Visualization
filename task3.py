import bpy
from mathutils import *
from math import *

# Initial data
q = Quaternion((1,0,0,0))
omega = Vector((2,1.5,0.25))
f = Vector((0,0,1))
p = Vector((0,0,0.5))

# Variable for currently active object
myobj = bpy.data.objects['O']
myobj.rotation_mode = 'QUATERNION'

# Clear all previous animation data
myobj.animation_data_clear()

# set first and last frame index
total_time = 12.5 # Animation should be 12.5 seconds long
fps = 24 # Frames per second (fps)
bpy.context.scene.frame_start = 0
bpy.context.scene.frame_end = int(total_time*fps)+1

# stepsize
h = 0.05

# loop of frames 
keyframe_freq = 1
nlast = bpy.context.scene.frame_end
for n in range(nlast):
    t = total_time*n/nlast
    # Do computations here...
    omega = omega + h*p.cross(q.conjugated()*f)
    dq = Quaternion(h*omega)
    q = q*dq
    # Check if n is a multiple of keyframe_freq
    if n%keyframe_freq == 0:
        bpy.context.scene.frame_set(n)
        # Set current location like this
        myobj.rotation_quaternion = q
        # Insert new keyframe for "location" like this
        myobj.keyframe_insert(data_path="rotation_quaternion")