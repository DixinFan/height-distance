import cv2
import numpy as np
cap = cv2.VideoCapture(0)

def undistort(frame):
    fx = 519.001212946671
    cx = 313.102107496223
    fy = 518.130506806157
    cy = 253.915619442965
    k1, k2, p1, p2, k3 = 0.0314412066449391, -0.0540760680743840, 0.0, 0.0, 0.0


    # 相机坐标系到像素坐标系的转换矩阵
    k = np.array([
        [fx, 0, cx],
        [0, fy, cy],
        [0, 0, 1]
    ])
    # 畸变系数
    d = np.array([
        k1, k2, p1, p2, k3
    ])
    h, w = frame.shape[:2]
    mapx, mapy = cv2.initUndistortRectifyMap(k, d, None, k, (w, h), 5)
    return cv2.remap(frame, mapx, mapy, cv2.INTER_LINEAR)


while(cap.isOpened()):
    ret, frame = cap.read()

    cv2.imshow('frame', undistort(frame))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
