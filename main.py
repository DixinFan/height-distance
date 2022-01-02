from detect_faces import *
from caculate_depth import *
from calibrate_parameters import *

face_model = get_face_detector()
# landmark_model = get_landmark_model()
cap_left = cv2.VideoCapture(0)
cap_right = cv2.VideoCapture(2)

ret, img = cap_left.read()
h, w = img.shape[:2]

real_height = 0
stable_distance = 0

while (True):
    ret, img_left = cap_left.read()
    ret, img_right = cap_right.read()
    rects_left = find_faces(img_left, face_model)
    rects_right = find_faces(img_right, face_model)
    amount_faces_left = len(rects_left)
    amount_faces_right = len(rects_right)

    if amount_faces_left == 0 or amount_faces_right == 0:
        pass
    elif amount_faces_left != amount_faces_right:
        pass
    else:
        y_left, center_point_left, center_point_right = caculate_center_point(img_left, img_right, rects_left, rects_right)
        depth = calc_depth(center_point_right, center_point_left, img_right, img_left)
        # marks_left = detect_marks(img_left, landmark_model, rect_left)
        # draw_marks(img_left, marks_left)
        depth = calibrate_depth(depth)

        if abs(depth-80) <= 10:
            scale_y_left = y_left / h
            real_height = caculate_height(scale_y_left)

        if depth > 82:
            real_height = 0

        if abs(stable_distance - depth) >= 20:
            stable_distance = depth

        cv2.putText(img_left, "Height: " + str(round(real_height, 1)), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
        cv2.putText(img_right, "Distance: " + str(round(stable_distance, 1)), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)

    cv2.imshow("img_left", img_left)
    cv2.imshow("img_right", img_right)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap_left .release()
cap_right .release()
cv2.destroyAllWindows()