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


while True:
    ret, img = cap.read()
    h, w = img.shape[:2]
    rects = find_faces(img, face_model)
    rects = scalize_rects(h, w, rects)
    rects = remove_edge_rect(rects)
    if len(rects) > 0:
        rect, area = choose_largest_rect(rects)
        draw_face_rect(img, rect)
    cv2.imshow("img", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()




