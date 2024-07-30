import cv2
import pyautogui
import numpy as np


def print_c(clignotant):
    clignotant = str(clignotant)
    # os.system("clear")
    print("\033[5;34;42m"+clignotant+"\033[0m")

    pass


def capture_opencv(capture_width,capture_height):

    screenshot = pyautogui.screenshot()
    frame = np.array(screenshot)
    frame = cv2.resize(frame, (capture_width, capture_height))

    return frame





def main():





    while True:
        frame = capture_opencv(640,320)
        
        cv2.imshow('Screen Capture', frame)
 
    # 按'q'键退出循环
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break



        pass
            # nm_bag = nm_bag - 1

    # domTree.write("out.osm",encoding="utf8")
 
if __name__=="__main__":
    main()
    pass
