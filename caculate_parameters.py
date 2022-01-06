from detect_faces import *
from calibrate_parameters import *

face_model = get_face_detector()
color = (0, 255, 0)

base_distance = 80
bias_distance = 10

stable_distance_base = 15


def stablelize_depth(distance, depth):
    if abs(distance - depth) > stable_distance_base:
        distance = depth
        distance = round(distance, 1)
    return distance


def caculate_height(depth, scale_y_left, height, count_height, sum_height):
    if (depth == 0) or (depth > (base_distance + bias_distance)):
        height, count_height, sum_height = 0, 0, 0
    elif abs(depth-base_distance) <= bias_distance:
        count_height = count_height + 1
        sum_height = sum_height + calibrate_height(scale_y_left)
    else:
        if count_height > 0:
            height = round(sum_height/count_height, 1)
        else:
            if height > 0:
                pass
            else:
                height = -1
        count_height, sum_height = 0, 0
    return height, count_height, sum_height


def caculate_params(img_left, img_right):
    h, w = img_left.shape[:2]
    rects_left = find_faces(img_left, face_model)
    rects_right = find_faces(img_right, face_model)
    rects_left = remove_edge_rects(w, rects_left)
    rects_right = remove_edge_rects(w, rects_right)
    if (len(rects_left) != len(rects_right)) or (len(rects_left) == 0):
        return 0, 0
    else:
        rect_left, area_left = choose_largest_rect(rects_left)
        rect_right, area_right = choose_largest_rect(rects_right)
        draw_rect(img_left, rect_left)
        draw_rect(img_right, rect_right)
        x_left = caculate_rect_x_center(rect_left)
        x_right = caculate_rect_x_center(rect_right)
        y_left = caculate_rect_y_center(rect_left)
        depth = caculate_depth(w, x_left, x_right)
        depth = calibrate_depth(depth)
        scale_y_left = y_left / h
    return depth, scale_y_left


def remove_edge_rects(w, rects):
    for rect in rects:
        scale_x = rect[0] / w
        if abs(scale_x-0.5) > 0.25:
            rects.remove(rect)
    return rects


def draw_rect(img, rect):
    cv2.rectangle(img, (rect[0],rect[1]), (rect[2],rect[3]), color, 2)


def caculate_rect_x_center(rect):
    return rect[0] + (rect[2] - rect[0]) / 2


def caculate_rect_y_center(rect):
    return rect[1] + (rect[3] - rect[1]) / 2


def caculate_depth(width, x_left, x_right, baseline=9, alpha=88):
    # CONVERT FOCAL LENGTH f FROM [mm] TO [pixel]:
    f_pixel = (width * 0.5) / np.tan(alpha * 0.5 * np.pi / 180)
    # CALCULATE THE DISPARITY:
    disparity = x_left - x_right
    depth = (baseline * f_pixel) / disparity
    return depth


def choose_largest_rect(rects):
    rects_area = []
    for rect in rects:
        rects_area.append((rect[2] - rect[0]) * (rect[3] - rect[1]))
    max_value = max(rects_area)
    max_index = rects_area.index(max_value)
    return rects[max_index], max_value
