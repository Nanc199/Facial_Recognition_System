import cv2

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

capture = cv2.VideoCapture(0)

while True:
    x, frame = capture.read()

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    roi = face_detector.detectMultiScale(gray_frame, 1.2, 3)

    # print(roi)

    for x, y, w, h in roi:
        cv2.rectangle(frame, (x, y), (x+h, y+w), (22,22,23), 2)

    cv2.putText(frame, text = f"Number of Persons : {len(roi)}", org = (20, 20), fontFace = 2, fontScale = 1.1, color = (22,22,23), thickness = 3)


    cv2.imshow("Read faces", frame)

    if cv2.waitKey(20) & 0xff == ord("w"):
        break