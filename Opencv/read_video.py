import cv2
cap = cv2.VideoCapture(r"C:\Users\priya\Downloads\naturevid.mp4")
while True:
    is_True,frame = cap.read()
    
    cv2.imshow("naturevid",frame)
    
    cv2.waitKey(0)