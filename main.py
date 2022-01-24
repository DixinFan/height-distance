from caculate_parameters import *
from calibrate_parameters import *

color = (0, 255, 0)
font = cv2.FONT_HERSHEY_SIMPLEX
cap_left = cv2.VideoCapture(2)
cap_right = cv2.VideoCapture(0)

height = 0
distance = 0

count_height = 0
sum_height = 0


while True:
    ret, img_left = cap_left.read()
    ret, img_right = cap_right.read()
    depth, scale_y_left = caculate_params(img_left, img_right)

    # height, count_height, sum_height = caculate_height(depth, scale_y_left, height, count_height, sum_height)

    # distance = stablelize_depth(distance, depth)
    distance =  round(depth, 0)
    if abs(distance - 180) <= 1:
    # if distance == 160.0:
        print(scale_y_left)
        # distance = scale_y_left
    # else:
    #     distance = 0

    cv2.putText(img_left, "height: " + str(height), (50, 50), font, 1.2, color, 3)
    cv2.putText(img_right, "distance: " + str(distance), (50, 50), font, 1.2, color, 3)
    cv2.imshow("img_left", img_left)
    cv2.imshow("img_right", img_right)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap_left .release()
cap_right .release()
cv2.destroyAllWindows()