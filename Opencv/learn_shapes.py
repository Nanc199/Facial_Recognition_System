
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Could not access webcam")
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Detect edges
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours
    contours, _ = cv2.findContours(
        edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    for contour in contours:
        # Ignore very small objects/noise
        area = cv2.contourArea(contour)

        if area < 500:
            continue

        # Approximate the contour
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.04 * perimeter, True)

        # Number of corners
        corners = len(approx)

        # Get position
        x, y, w, h = cv2.boundingRect(approx)

        # Identify shape
        if corners == 3:
            shape = "Triangle"
        elif corners == 4:
            # Check whether it is square or rectangle
            ratio = w / float(h)

            if 0.9 <= ratio <= 1.1:
                shape = "Square"
            else:
                shape = "Rectangle"
        elif corners == 5:
            shape = "Pentagon"
        elif corners > 5:
            shape = "Circle"

        # Draw contour
        cv2.drawContours(frame, [approx], -1, (0, 255, 0), 3)

        # Write shape name
        cv2.putText(
            frame,
            shape,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    cv2.imshow("Shape Detection", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()