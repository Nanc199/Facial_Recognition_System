import cv2
img = cv2.imread(r"C:\Users\priya\Downloads\image.jpg")


cv2.putText(img,"Hello World",(300,100),2,1.0,(23,183,29),4)
cv2.imshow("image",img)


cv2.waitKey(0)