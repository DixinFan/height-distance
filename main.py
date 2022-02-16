from caculate_parameters import *

color = (0, 255, 0)
font = cv2.FONT_HERSHEY_SIMPLEX
cap_left = cv2.VideoCapture(0)
cap_right = cv2.VideoCapture(1)

while True:
    ret, img_left = cap_left.read()
    ret, img_right = cap_right.read()

    distance, scale_y_left = caculate_params(img_left, img_right)
    distance, height = caculate_height(distance, scale_y_left)

    cv2.putText(img_left, "height: " + str(height), (50, 50), font, 1.2, color, 3)
    cv2.putText(img_right, "distance: " + str(distance), (50, 50), font, 1.2, color, 3)
    cv2.imshow("img_left", img_left)
    cv2.imshow("img_right", img_right)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap_left.release()
cap_right.release()
cv2.destroyAllWindows()
