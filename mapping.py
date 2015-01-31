from sr.robot import *
from math import sin, cos, pi
import arena

def test():
    R = Robot()
    markers = R.see()
    calculate_location(marker_list)

# Call this one please ty
def calculate_location(marker_list):
    points = [_find_location(marker) for marker in markers if marker < 20]
    return _calculate_average_location(points)

def _calculate_average_location(xy_list):
    tot_x, tot_y = 0,0
    for point in xy_list:
        tot_x += point.x
        tot_y += point.y

    # Return a tuple location, or None if the list was empty!
    if len(xy_list) == 0: return None 
    return ((tot_x/len(xy_list)),(tot_y/len(xy_list)))

def _find_location(marker):
    marker_x = markers_table_coords[marker.id][0] # LOOK UP USING HARRY'S CODE
    marker_y = markers_table_coords[marker.id][1] # LOOK UP USING HARRY'S CODE
    marker_rotation = markers_table_coords[marker.id][2] # LOOK UP USING HARRYS CODE

    marker_relative_angle = marker.orientation.rot_y

    # Theta
    marker_to_north = pi - (marker_rotation - marker_relative_angle)

    marker_distance = marker.dist

    x = marker_distance*cos(pi/2 - marker_to_north)
    y = marker_distance*sin(pi/2 - marker_to_north)
    angle = marker_relative_angle - marker_to_north

    return (x+marker_x,y+marker_y,angle)