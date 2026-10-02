import cv2
img = cv2.imread(r"C:\Users\priya\Downloads\image.jpg")
cv2.imshow("image",img)


gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gimage",gray_img)


hls_img = cv2.cvtColor(img,cv2.COLOR_BGR2HLS)
cv2.imshow("himage",hls_img)


cv2.waitKey(0)