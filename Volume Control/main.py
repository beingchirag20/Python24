import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Set up the camera width and height
wCAM, hCam = 640, 480

# Initialize the webcam
cap = cv2.VideoCapture(0)
cap.set(3, wCAM)
cap.set(4, hCam)

# Create a hand detector object
detector = htm.HandDetector(detectionCon=0.7)

# Pycaw setup for volume control
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# Get the current volume range
volRange = volume.GetVolumeRange()
minvol = volRange[0]
maxvol = volRange[1]

vol = 0
volBar = 400
volPer = 0

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmlist = detector.findPosition(img, draw=False)

    if len(lmlist) != 0:
        # Coordinates for thumb tip and index finger tip
        x1, y1 = lmlist[4][1], lmlist[4][2]
        x2, y2 = lmlist[8][1], lmlist[8][2]

        # Midpoint of the line between the thumb and index finger
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        # Draw circles on the thumb and index finger tips
        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        # Calculate the length between the two points
        length = math.hypot(x2 - x1, y2 - y1)

        # Convert length to volume
        vol = np.interp(length, [50, 300], [minvol, maxvol])
        volBar = np.interp(length, [50, 300], [400, 150])
        volPer = np.interp(length, [50, 300], [0, 100])
        volume.SetMasterVolumeLevel(vol, None)

        # Change color if volume is at minimum
        if length < 50:
            cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)

    # Display volume bar
    cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED)
    cv2.putText(img, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

    cv2.imshow("Img", img)
    cv2.waitKey(1)
