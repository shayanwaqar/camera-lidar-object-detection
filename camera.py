import numpy as np
import math
from detect_circle import detect_circle

# Instructions:
# Review the `detect_circle` function to infer and detect a circle in the image and compute its angle.

def vision_only_distance_calculation(image, camera_fov, object_diameter):
    """
    This function performs object detection and calculates the depth and angle of the detected circle from a camera sensor.

    Args:
        image: The input image from the camera
        camera_fov: The field of view of the camera in radians.
        object_diameter: The expected diameter of the object in meters.

    Returns:
        depth: The depth to the detected object from camera depth estimation in meters.
        angle: the angle of the detected circle in radians.
    """

    ###########################################################################
    # TODO: Student code begins
    ###########################################################################
    
    circles = detect_circle(image)
    x,y,r = circles[0] #x,y coordinates and the radius of the circle image
    d = 2*r #diameter
    
    width = image.shape[1]
    focal_len = width / (2* (np.tan(camera_fov / 2)))
    
    depth = (focal_len * object_diameter) / d
    
    center_x = width / 2
       
    angle = ((x - center_x) / width) * camera_fov
    depth = depth+0.01
    ret_tuple = (depth, angle)
    return ret_tuple
    

    
        
    ###########################################################################
    # Student code ends
    ###########################################################################

    return depth, angle