## GPS Coordinate Transformation Algorithm
## Written by Thanapol Supitayakul
import math
import numpy as np

yaw = math.radians(0)                                           # Camera heading when taking a picture in degree
fovx = math.radians(73.74)                                      # Camera's field of view or angle of view in degrees
fovy = math.radians(53.13)
x = 1442                                                        # x-coordinate of the object
y =  545                                                        # y-coordinate of the object

## Read
fp = open('target_frame_00000000GPS.txt','r')                   # Insert file name 
frame = fp.readline()
lon = fp.readline()
lat = fp.readline()
alt = fp.readline() 
lon = float(''.join(filter(lambda x: x in '.0123456789', lon))) # Cut out the word and join digits together then convert to float
lat = float(''.join(filter(lambda x: x in '.0123456789', lat)))
alt = float(''.join(filter(lambda x: x in '.0123456789', alt)))
fp.close()
picpos = [lon,lat]


## Transform
altSI = (alt-6.5)*0.3048                                        # Convert alttitude from feet to meter
a = 2*altSI/(np.cos(fovx/2))
b = 2*altSI/(np.cos(fovy/2))
scalex = a/1920                                                 # Scale to pixel
scaley = b/1080
offset = [scalex * x,scaley * y]                                # Scale position in pixel to physical unit
rot = [[np.cos(yaw),-np.sin(yaw)],[np.sin(yaw),np.cos(yaw)]]    # Calculate for rotation matrix
pos = np.dot(rot,offset)                                        # Scale the magnitude of an offset matrix to the north-east 
posm = (1/110947.2) * pos                                       # Scale the magnitude of a position matrix with reference to 
objpos = picpos + posm                                          # Shift original gps coordinate to the object coordinate
print(objpos)