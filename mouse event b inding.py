import cv2
import numpy as np


"""
def draw(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:  # Corrected typo here
        cv2.circle(img, (x, y), 100, (125, 0, 255), 5)
    if event == cv2.EVENT_RBUTTONDBLCLK:  # Right mouse button double-click
        cv2.rectangle(img, (x, y), (x + 100, y + 75), (125, 125, 255), 2)

cv2.namedWindow(winname="res")
img = np.zeros((512, 512, 3), np.uint8)
cv2.setMouseCallback("res", draw)

while True:
    cv2.imshow("res", img)
    if cv2.waitKey(1) & 0xFF == 27:  # Exit on pressing 'Esc'
        break

cv2.destroyAllWindows()
"""

#Create A function e=which help to find coordinate of any pixel and its color
import cv2
import numpy as np

def mouse_event(event, x, y, flags, param):
    print("event==", event)
    print("x==", x)
    print("y==", y)
    print("flags==", flags)
    print("param==", param)
    
    font = cv2.FONT_HERSHEY_PLAIN
    
    if event == cv2.EVENT_LBUTTONDOWN:  # Left button down
        print(x, ',', y)
        cord = str(x) + ',' + str(y)
        cv2.putText(img, cord, (x, y), font, 1, (155, 125, 100), 2)
        cv2.imshow('res', img)
    
    if event == cv2.EVENT_RBUTTONDOWN:  # Right button down
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        color_bgr = str(b) + ', ' + str(g) + ', ' + str(r)
        cv2.putText(img, color_bgr, (x, y), font, 1, (155, 125, 100), 2)
        cv2.imshow('res', img)

# Create a black image
cv2.namedWindow(winname="res")
img = np.zeros((512, 512, 3), np.uint8)  # Use np.uint8 for image data

# Set mouse callback function
cv2.setMouseCallback("res", mouse_event)

while True:
    cv2.imshow("res", img)
    if cv2.waitKey(1) & 0xFF == 27:  # Exit on pressing 'Esc'
        break

cv2.destroyAllWindows()
