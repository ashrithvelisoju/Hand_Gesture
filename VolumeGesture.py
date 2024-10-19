import cv2
import mediapipe as mp
import numpy as np
import osascript
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None
)

volume = cast(interface, POINTER(IAudioEndpointVolume))

volume.GetMute()
#volume.GetMasterVolumeLevel()

vRange=volume.GetVolumeRange()
minv,maxv=vRange[0],vRange[1]
#volume.SetMasterVolumeLevel(-20.0, None)
mp_hands = mp.solutions.hands
draw=mp.solutions.drawing_utils

hands = mp_hands.Hands()
caputure = cv2.VideoCapture(0)
while True:
    value,image = caputure.read()
    rgbimage = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    processed_image = hands.process(rgbimage)
    print(processed_image.multi_hand_landmarks)
    if(processed_image.multi_hand_landmarks):
        for handLandmarks in processed_image.multi_hand_landmarks:
            for finger_id,landmark_co in enumerate(handLandmarks.landmark):
                #print(enumerate,landmark_co)
                height,width,channel = image.shape
                cx,cy = int(landmark_co.x * width), int(landmark_co.y * height)
                #print(finger_id,cx,cy)
                if finger_id == 4:
                    cv2.circle(image,(cx,cy),30,(255,0,255),cv2.FILLED)
                    tpx,tpy=cx,cy
                if finger_id==8:
                    cv2.circle(image,(cx,cy),30,(255,0,255),cv2.FILLED)
                    ipx,ipy=cx,cy
                    cv2.line(image,(tpx,tpy),(ipx,ipy),(0,255,0),9)
                    distance=math.sqrt((ipx-tpx)**2+(ipy-tpy)**2)
                    print(distance)
                    v=np.interp(distance,[25,250],[minv,maxv])
                    volume.SetMasterVolumeLevel(v, None)
                    vol="set volume output volume "+str(v)
                    #osascript.osascript(vol)
            draw.draw_landmarks(image,handLandmarks,mp_hands.HAND_CONNECTIONS,
                        
                                )

    cv2.imshow('Mediapipe Hands',cv2.flip(image,1))
    if cv2.waitKey(1) & 0xFF==27:
        break
caputure.release()
cv2.destroyAllWindows()