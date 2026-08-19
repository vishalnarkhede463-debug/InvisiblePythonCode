# I have added comments as well for better understanding
#for first 3 seconds after the camera starts , be out of the frame and let it capture the background image


import cv2
import numpy as np
import time

print("Starting blue invisibility cloak... Press 'q' to quit.")

# Open camera
cap = cv2.VideoCapture(0)

time.sleep(3)

# Take a picture of the background before starting
background = 0

for i in range(30):
    ret, background = cap.read()

    if not ret:
        print("Couldn't capture the background.")
        cap.release()
        exit()

# Mirror the background
background = np.flip(background, axis=1)

while cap.isOpened():

    ret, img = cap.read()

    if not ret:
        break

    # Mirror the live video
    img = np.flip(img, axis=1)

    # HSV makes it easier to detect a particular color
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Blue color range
    lower_blue = np.array([90, 80, 80])
    upper_blue = np.array([130, 255, 255])

    # Find the blue parts of the image
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Clean up the mask a little
    kernel = np.ones((3, 3), np.uint8)

    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)

    # Reverse the mask so we can keep everything except the cloak
    mask_inv = cv2.bitwise_not(mask)

    # Put the old background where the blue cloak is
    background_part = cv2.bitwise_and(
        background,
        background,
        mask=mask
    )

    # Keep the current frame everywhere else
    current_part = cv2.bitwise_and(
        img,
        img,
        mask=mask_inv
    )

    # Join both parts together
    final_output = cv2.addWeighted(
        background_part,
        1,
        current_part,
        1,
        0
    )

    cv2.imshow("Blue Invisibility Cloak", final_output)

    # Press q to close
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()