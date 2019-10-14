import cv2

cascade_src = 'data/cascade.xml'
video_src = 'road_traffic.mp4'

cap = cv2.VideoCapture(video_src)
car_cascade = cv2.CascadeClassifier(cascade_src)

while True:
    ret, img = cap.read()

    roi = img[280:,:]
    
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    
    cars = car_cascade.detectMultiScale(gray, 6, 15)

    for (x,y,w,h) in cars:
        cv2.rectangle(roi,(x,y),(x+w,y+h),(0,0,255),2)      
    
    cv2.imshow('video', img)
    
    if cv2.waitKey(10) == ord('q'):
        break

cv2.destroyAllWindows()