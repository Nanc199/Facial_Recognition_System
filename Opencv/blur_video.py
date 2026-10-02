import cv2
cap = cv2.VideoCapture(0)

while True:
    x,frame = cap.read()
    
    cv2.imshow("vid",frame)
    
    black_vid = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("blvid",black_vid)
    
    blur = cv2.GaussianBlur(frame,(15,15),1.0)
    cv2.imshow("bluvid",blur)
    
    edges = cv2.Canny(frame,300,200)
    cv2.imshow("evid",edges)
    
    if cv2.waitKey(20) & 0xff == ord("x"):
        break
    
    cv2.waitKey(20)