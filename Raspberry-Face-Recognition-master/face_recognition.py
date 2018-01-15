# Import OpenCV2 for image processing
import cv2

# Import numpy for matrices calculations
import numpy as np

# Create Local Binary Patterns Histograms for face recognization
recognizer = cv2.face.createLBPHFaceRecognizer()

# Load the trained mode
recognizer.load('trainer/trainer.yml')

# Load prebuilt model for Frontal Face
cascadePath = "/home/pi/opencv-3.2.0/data/haarcascades/haarcascade_frontalface_alt.xml"

# Create classifier from prebuilt model
faceCascade = cv2.CascadeClassifier(cascadePath);

# Set the font style
font = cv2.FONT_HERSHEY_SIMPLEX

# Initialize and start the video frame capture
cam = cv2.VideoCapture(0)

# Loop
while True:
    # Read the video frame
    ret, im =cam.read()

    # Convert the captured frame into grayscale
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    # Get all face from the video frame
    faces = faceCascade.detectMultiScale(gray, 1.2,5)

    # For each face in faces
    for(x,y,w,h) in faces:

        # Create rectangle around the face
        cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)

        # Recognize the face belongs to which ID
        Id, www = recognizer.predict(gray[y:y+h,x:x+w])

        # Check the ID if exist 
        if(Id == 1):
            Id = "Chelsea"
        elif(Id == 2):
            Id = "BaiBai"
        elif(Id == 3):
            Id = "Nicole"
        elif(Id == 4):
            Id = "Peter"
        elif(Id == 5):
            Id = "Jack"
        elif(Id == 6):
            Id = "Dorothy"
        else:
	    Id = "Unknow"

        # Put text describe who is in the picture
        cv2.rectangle(im, (x-22,y-60), (x+w+22, y-22), (0,166,166), 2)
        cv2.putText(im, str(Id), (x,y-30), font, 1, (255,255,255), 2)
        print Id
    # Display the video frame with the bounded rectangle
    cv2.imshow('im',im) 

    # If 'q' is pressed, close program
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Stop the camera
cam.release()

# Close all windows
cv2.destroyAllWindows()
