import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # set Width
cap.set(4, 480)  # set Height
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
face_id = input("Enter the Name of the person: ")

count = 0
while True:
    ret, frame = cap.read()  # Flip camera vertically
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        if cv2.waitKey(26) in [ord('q'), 27]:
            cv2.imwrite("./facerecdataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y + h, x:x + w])
            count += 1

        cv2.imshow('frame', frame)
        cv2.imshow('gray', gray)

    k = cv2.waitKey(30) & 0xff

    if count >= 100:
        break
cap.release()
cv2.destroyAllWindows()