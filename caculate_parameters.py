from detect_faces import *
from calibrate_parameters import *
from predict_height import *

face_model = get_face_detector()
color = (0, 255, 0)
x_threshold = 0.2
y_threshold = 0.1


def caculate_height(distance, scale_y_left):

    if distance == 0 or scale_y_left == 0:
        height = 0
    else:
        x = z_score_normalize(scale_y_left, 'x')
        y = z_score_normalize(distance, 'y')
        height = poly(x, y)
        height = height + 8
        bias = (distance - 120) / 20
        height = height + bias

    if distance > 100 or distance < 50:
        distance = 0
        height = 0

    return distance, height


def scalize_rects(h, w, rects):
    for rect in rects:
        rect[0], rect[1], rect[2], rect[3] = rect[0] / w, rect[1] / h, rect[2] / w, rect[3] / h
    return rects


def remove_edge_rect(rects):
    for rect in rects:
        x_start, y_start, x_end, y_end = rect[0], rect[1], rect[2], rect[3]
        if x_start - x_threshold < 0 or x_end + x_threshold > 1 or y_start - y_threshold < 0 or y_end + y_threshold > 1:
            rects.remove(rect)
    return rects


def draw_face_rect(img, rect):
    h, w = img.shape[:2]
    x_start, y_start, x_end, y_end = rect[0]*w, rect[1]*h, rect[2]*w, rect[3]*h
    x_start, y_start, x_end, y_end = int(x_start), int(y_start), int(x_end), int(y_end)
    cv2.rectangle(img, (x_start, y_start), (x_end, y_end), color, 2)


def caculate_params(img_left, img_right):
    h, w = img_left.shape[:2]

    rects_left = find_faces(img_left, face_model)
    rects_right = find_faces(img_right, face_model)

    rects_left = scalize_rects(h, w, rects_left)
    rects_right = scalize_rects(h, w, rects_right)

    rects_left = remove_edge_rect(rects_left)
    rects_right = remove_edge_rect(rects_right)

    if (len(rects_left) != len(rects_right)) or (len(rects_left) == 0):
        return 0, 0
    else:
        rect_left, area_left = choose_largest_rect(rects_left)
        rect_right, area_right = choose_largest_rect(rects_right)

        draw_face_rect(img_left, rect_left)
        draw_face_rect(img_right, rect_right)

        x_left = caculate_rect_x_center(rect_left)
        x_right = caculate_rect_x_center(rect_right)
        y_left = caculate_rect_y_center(rect_left)

        depth = caculate_depth(w, x_left*w, x_right*w)
        depth = calibrate_depth(depth)

    return depth, y_left


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
