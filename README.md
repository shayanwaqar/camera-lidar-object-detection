camera_only.py
This script performs object detection using only camera data. It:

Uses detect_circle to detect a circular object in an image.
Estimates the depth (distance) of the object using focal length and object diameter.
Computes the angle of the detected object relative to the center of the image.
Returns the estimated depth and angle of the object.

camera_and_lidar.py
This script combines camera and LiDAR data to detect and classify objects. It:

Uses the detect_circle function to detect a circular object in an image.
Computes the object's angle relative to the camera's field of view.
Maps this angle to LiDAR distance data.
Uses LiDAR readings to classify the object as either a "sphere" or "disk" based on standard deviation calculations of nearby LiDAR points.
