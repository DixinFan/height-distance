from caculate_parameters import *

face_model = get_face_detector()
cap = cv2.VideoCapture(0)
x_threshold = 0.2
y_threshold = 0.1


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


# def z_score_normalize(data, dim):
#     mean, std = 0, 0
#     if dim == 'x':
#         mean = 0.03204
#         std = 0.02154
#     if dim == 'y':
#         mean = 0.5243
#         std = 0.09587
#     data = (data - mean) / std
#     return data
#
#
# def poly(x, y):
#     p00 = 169.3
#     p10 = -2.179
#     p01 = -7.568
#     p20 = 0.6889
#     p11 = 3.067
#     p02 = 0.8354
#     p21 = -0.9831
#     p12 = -0.1675
#     p03 = 0.3497
#     height = p00 + p10 * x + p01 * y + p20 * x ** 2 + p11 * x * y + p02 * y ** 2 + p21 * x ** 2 * y + p12 * x * y ** 2 + p03 * y ** 3
#     return height

def z_score_normalize(data, dim):
    mean, std = 0, 0
    if dim == 'x':
        mean = 0.03204
        std = 0.02154
    if dim == 'y':
        mean = 0.5243
        std = 0.09587
    data = (data - mean) / std
    return data


def poly(x, y):
    p00 = 77.78
    p10 = -41.44
    p01 = -3.152
    p20 = 13
    p11 = -2.548
    p02 = 0.6713
    p21 = 2.064
    p12 = 2.213
    p03 = 2.284
    height = p00 + p10 * x + p01 * y + p20 * x ** 2 + p11 * x * y + p02 * y ** 2 + p21 * x ** 2 * y + p12 * x * y ** 2 + p03 * y ** 3
    return height

while True:
    ret, img = cap.read()
    h, w = img.shape[:2]
    rects = find_faces(img, face_model)
    rects = scalize_rects(h, w, rects)
    rects = remove_edge_rect(rects)
    if len(rects) > 0:
        print("start")
        rect, area = choose_largest_rect(rects)
        print(area)
        y_left = caculate_rect_y_center(rect)
        print(y_left)
        x = z_score_normalize(area, 'x')
        y = z_score_normalize(y_left, 'y')
        height = poly(x, y)
        print(height)

        draw_face_rect(img, rect)
    cv2.imshow("img", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()




