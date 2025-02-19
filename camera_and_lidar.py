import math
import numpy as np
from detect_circle import detect_circle

# Instructions:
# Step 1: Review the detect_circle function to infer and detect a circle in the image 
#         and compute its angle.
# Step 2: Explore the LiDAR data corresponding to the detected object. Investigate 
#         how to classify the object as either a sphere or a disk. You may reuse 
#         your code from camera_only.py.

def camera_and_lidar_calculation(image, camera_fov, object_diameter, lidar_data):
    """
    Performs object detection and classification by combining data from a camera and a LiDAR sensor.

    Args:
        image: The input image captured by the camera.
        camera_fov: The field of view of the camera in radians.
        object_diameter: The expected diameter of the object in meters.
        lidar_data: An array representing LiDAR distance data indexed by angle 
                                  in degrees, where each element corresponds to the distance 
                                  at a specific angle.

    Returns:
        lidar_distance: The distance to the detected object from the LiDAR sensor in meters.
        object_shape: A string indicating the shape of the detected object ("sphere" or "disk").
    """

    ###########################################################################
    # TODO: Student code begins
    ###########################################################################

    # Get the values from the circle
    circle = detect_circle(image)[0]
    x, y, radius = circle

    # Get image width and calculate the angle_to_object
    width = image.shape[1]
    angle_to_object = ((x - (width / 2)) / width) * camera_fov

    # Calculate Depth
    lidar_idx = round(math.degrees(angle_to_object)) % 360
    lidar_distance = lidar_data[lidar_idx]

    # Get the five points before and after the LiDAR angle index and filter out too far
    five_before = lidar_data[lidar_idx - 5 : lidar_idx]
    five_after = lidar_data[lidar_idx : lidar_idx + 5]

    negative_filtered = [x for x in five_before if (abs(x - lidar_distance) < 0.13)]
    positive_filtered = [x for x in five_after if abs(x - lidar_distance) < 0.13]

    # Find the STD and use that to determine shape
    negative_deviation = np.std(negative_filtered)
    positive_deviation = np.std(positive_filtered)

    if negative_deviation < 0.005 and positive_deviation < 0.005:
        object_shape = "disk"
    else:
        object_shape = "sphere"

    ###########################################################################
    # Student code ends
    ###########################################################################

    return lidar_distance, object_shape
