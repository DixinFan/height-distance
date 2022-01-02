import sys
import cv2
import numpy as np
import time

color = (0, 255, 0)

def calc_depth(right_point, left_point, frame_right, frame_left, baseline=9, alpha=88):

    # CONVERT FOCAL LENGTH f FROM [mm] TO [pixel]:
    height_right, width_right, depth_right = frame_right.shape
    height_left, width_left, depth_left = frame_left.shape

    if width_right == width_left:
        f_pixel = (width_right * 0.5) / np.tan(alpha * 0.5 * np.pi/180)

    else:
        print('Left and right camera frames do not have the same pixel width')

    x_right = right_point[0]
    x_left = left_point[0]

    # CALCULATE THE DISPARITY:
    disparity = x_left-x_right      #Displacement between left and right frames [pixels]

    # CALCULATE DEPTH z:
    zDepth = (baseline*f_pixel)/disparity             #Depth in [cm]

    return zDepth

def caculate_center_point(img_left, img_right, rects_left, rects_right):
    rect_left = rects_left[0]
    rect_right = rects_right[0]

    cv2.rectangle(img_left, (rect_left[0], rect_left[1]), (rect_left[2], rect_left[3]), color, 2)
    cv2.rectangle(img_right, (rect_right[0], rect_right[1]), (rect_right[2], rect_right[3]), color, 2)

    x_left = rect_left[0] + (rect_left[2] - rect_left[0]) / 2
    y_left = rect_left[1] + (rect_left[3] - rect_left[1]) / 2
    center_point_left = (x_left, y_left)

    x_right = rect_right[0] + (rect_right[2] - rect_right[0]) / 2
    y_right = rect_right[1] + (rect_right[3] - rect_right[1]) / 2
    center_point_right = (x_right, y_right)

    return y_left, center_point_left, center_point_right

