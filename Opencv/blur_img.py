

import cv2

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Could not access webcam")
        break

    # Blur the webcam frame
    blurred = cv2.GaussianBlur(frame, (21, 21), 0)

    # Show the blurred video
    cv2.imshow("Blurred Webcam", blurred)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()