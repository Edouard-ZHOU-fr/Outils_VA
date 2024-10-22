import cv2
import time
import numpy as np


"""
python3 -c "import cv2; print(cv2.__version__)"

"""


def print_reussi(reussi):
    reussi = str(reussi)
    # os.system("clear")
    print("\033[1;32;47m"+reussi+"\033[0m")
    pass

def print_c(clignotant):
    clignotant = str(clignotant)
    # os.system("clear")
    print("\033[5;34;42m"+clignotant+"\033[0m", end='\r')
    pass


cap = cv2.VideoCapture(0)
#############################################################################


model_MOG2 = cv2.createBackgroundSubtractorMOG2(varThreshold=30,detectShadows=True)


#############################################################################


kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
model_KNN = cv2.createBackgroundSubtractorKNN() 

#############################################################################
 
while(1):
    ret, frame = cap.read()

    if ret: 
        fgmask1 = model_MOG2.apply(frame)
        # fgmask1 = model_KNN.apply(frame)
        fgmask1 = cv2.morphologyEx(fgmask1, cv2.MORPH_OPEN, kernel)
    
    else:
        print("Pas encore prete")
        continue



    
    contours = cv2.findContours(fgmask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    
    for c in contours:
        
        cv2.drawContours(frame,c,0,(0,0,255),3)
        
        # (x, y, w, h) = cv2.boundingRect(c)
        # cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)


        length = cv2.arcLength(c, True)
        if length > 100:
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

 
    cv2.imshow('org',frame)
    # cv2.imshow('MOG2_frame',fgmask)
    cv2.imshow('KNN_frame',fgmask1)

    if cv2.waitKey(1) & 0xFF == ord(' '):
        break


cap.release()
cv2.destroyAllWindows()






