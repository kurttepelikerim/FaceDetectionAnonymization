import cv2

#see: https://stackoverflow.com/questions/604749/how-do-i-access-my-webcam-in-python

cv2.namedWindow("preview")
vc = cv2.VideoCapture("video.mp4")
isBlur = False
isCanny = False

if vc.isOpened():
    rval, frame = vc.read()
else:
    rval = False
# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while rval:
    rval, frame = vc.read()
    blur_frame = cv2.blur(frame, (50,50))
    canny_frame = cv2.Canny(frame,50,150)
    #convert back to BGR
    canny_frame = cv2.cvtColor(canny_frame, cv2.COLOR_GRAY2BGR)
    # Convert into grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        if  isBlur:
            frame[y:y+h,x:x+w] = blur_frame[y:y+h,x:x+w]
        elif isCanny:
            frame[y:y + h, x:x + w] = canny_frame[y:y+h,x:x+w]
    # Display the output
    cv2.imshow('img', frame)
    # cv2.waitKey()
    key = cv2.waitKey(20)
    if key == 27:
        break
    elif key == ord('b'):
        isBlur = True
        isCanny = False
    elif key == ord('c'):
        isBlur = False
        isCanny = True
cv2.destroyWindow("preview")

