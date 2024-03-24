import cv2

def waitKey(window, key):
    while cv2.getWindowProperty(window, cv2.WND_PROP_VISIBLE) >= 1:
        keyValue = cv2.waitKey(1000) & 0xFF
        if (keyValue == key):
            cv2.destroyAllWindows()
            break