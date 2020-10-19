import numpy as np
import bmesh
import bpy
from math import *
from mathutils import *

#blend_dir = os.path.dirname(D/M.SC. prog. in Engineering Mathematics and Computational Science/Scientific Visualization/blender)
#if blend_dir not in sys.path:
#    sys.path.append(blend_dir)
#import rings
#import imp
#imp.reload(rings)

objs = bpy.data.objects

if objs.get("Cube") is not None:
    objs.remove(objs["Cube"], True)

def scenealreadyrendered():
    return(len(objs)==7)

if not scenealreadyrendered(): 
     
    # first delete previous objects
    candidate_list = [item.name for item in objs if item.type == "MESH"]

    # select them only.
    for object_name in candidate_list:
        objs[object_name].select = True

    # remove all selected.
    bpy.ops.object.delete()

    # remove the meshes, they have no users anymore.
    for item in bpy.data.meshes:
        bpy.data.meshes.remove(item)


# Gravitational constant when the mass of the sun is 1.
G = 2.95912208286e-4

# Planet names and order
#planets = ('Sun','Jupiter','Saturn','Uranus','Neptune','Pluto')

# The data below is obtained from here: https://ssd.jpl.nasa.gov/horizons.cgi

# Masses relative to the sun (the increased sun mass is to account for the inner planets)
masses = np.array([1.00000597682, 
                   0.000954786104043, 
                   0.000285583733151, 
                   0.0000437273164546, 
                   0.0000517759138449, 
                   6.571141277023631e-09])

# Positions of the planets in astronomical units (au) on September 5, 1994, at 0h00 GST.
positions = np.array([[0., 0., 0.],
                    [-3.502576677887171E+00, -4.111754751605156E+00,  9.546986420486078E-02],
                    [9.075323064717326E+00, -3.443060859273154E+00, -3.008002285860299E-01],
                    [8.309900066449559E+00, -1.782348877489204E+01, -1.738826162402036E-01],
                    [1.147049510166812E+01, -2.790203169301273E+01,  3.102324955757055E-01],
                    [-1.553841709421204E+01, -2.440295115792555E+01,  7.105854443660053E+00]])

# Velocities of the planets relative to the sun in au/day on September 5, 1994, at 0h00 GST.
velocities = np.array([[0., 0., 0.],
                    [5.647185685991568E-03, -4.540768024044625E-03, -1.077097723549840E-04],
                    [1.677252496875353E-03,  5.205044578906008E-03, -1.577215019146763E-04],
                    [3.535508197097127E-03,  1.479452678720917E-03, -4.019422185567764E-05],
                    [2.882592399188369E-03,  1.211095412047072E-03, -9.118527716949448E-05],
                    [2.754640676017983E-03, -2.105690992946069E-03, -5.607958889969929E-04]])

# Compute total linear momentum
ptot = (masses[:,np.newaxis]*velocities).sum(axis=0)

# Recompute velocities relative to the center of mass
velocities -= ptot/masses.sum()

# Linear momenta of the planets: p = m*v
momenta = masses[:,np.newaxis]*velocities

# Function for Newtonian acceleration field
def acc(x, masses = masses, G = G):
    N = masses.shape[0]
    d = x.shape[-1]
    dx_pairs = x[:, np.newaxis] - x[np.newaxis, :]
    msq_pairs = masses[:, np.newaxis]*masses[np.newaxis, :]
    
    # Remove self-self interactions
    dx_pairs = np.delete(dx_pairs.reshape((N*N,d)),slice(None,None,N+1), axis = 0).reshape((N,N-1,d))
    msq_pairs = np.delete(msq_pairs.reshape((N*N)),slice(None,None,N+1), axis = 0).reshape((N,N-1))
    
    # Compute pairwise distances
    dist_pairs = np.sqrt((dx_pairs**2).sum(axis=-1))
    
    # Compute the gravitational force using Newton's law
    forces = -G*(dx_pairs*msq_pairs[:,:,np.newaxis]/dist_pairs[:,:,np.newaxis]**3).sum(axis=1)
    
    # Return accelerations
    return forces/masses[:,np.newaxis]

# Select time step and total integration time (measured in days)
h = 100 # Time stepsize in days
totaltime = 100*365 # Total simulation time in days

# Preallocate output vectors at each step
t_out = np.arange(0.,totaltime,h)
x_out = np.zeros(t_out.shape + positions.shape, dtype=float)
x_out[0,:,:] = positions
v_out = np.zeros_like(x_out)
v_out[0,:,:] = velocities

# Use Symplectic Euler method for integration
for x0, x1, v0, v1 in zip(x_out[:-1],x_out[1:],v_out[:-1],v_out[1:]):
    x1[:,:] = x0 + h*v0
    v1[:,:] = v0 + h*acc(x1)
    
# -------------------------# Add the Blender code here

# Planet names and order
planets_names = ['Sun','Jupiter','Saturn','Uranus','Neptune','Pluto']
planets = []
for i in range(0, 6):
    bpyscene = bpy.context.scene
    # Create an empty mesh and the object.
    if not scenealreadyrendered():
        mesh = bpy.data.meshes.new('Sphere')
        basic_sphere = objs.new(planets_names[i],mesh)
        planets.append(basic_sphere)
        planets[i].location.x = positions[i][0]
        planets[i].location.y = positions[i][1]
        planets[i].location.z = positions[i][2]
    
        # bpy.context.object.data.name = "Cube1"
        # Add the object into the scene.
        bpyscene.objects.link(planets[i])
        bpyscene.objects.active = planets[i]
        planets[i].select = True

        bm = bmesh.new()
        bmesh.ops.create_uvsphere(bm, u_segments=32, v_segments=16, diameter=2)
        bm.to_mesh(mesh)
        bm.free()

        bpy.ops.object.modifier_add(type='SUBSURF')
        bpy.ops.object.shade_smooth()
        
        
        #mat = bpy.data.materials['Material']
        #tex = bpy.data.textures.new(planets[i], 'sunmapthumb.jpg')
        #slot = mat.texture_slots.add()
        #slot.texture = tex
  
        
# Clear all previous animation data
#objs.animation_data_clear()

# set first and last frame index
fps = 24 # Frames per second (fps)
bpy.context.scene.frame_start = 1
bpy.context.scene.frame_end = 365

# loop of frames and insert keyframes every 10th frame
keyframe_freq = 100
for n in t_out:
    # Check if n is a multiple of keyframe_freq
    if n%keyframe_freq == 0:
        # Set frame like this
        bpy.context.scene.frame_set(n//h)
        
        for planet in planets_names:
            myobj = bpy.data.objects[planet]
            # Set current location like this
            myobj.location = x_out[n//h,planets_names.index(planet),:]
            # Insert new keyframe for "location" like this
            myobj.keyframe_insert(data_path="location")
        
        