import cv2
import datetime
import os
import time
import sys
import numpy as np

def face(cam,outfile):
    anchor = 0
    recognizer = cv2.face.createLBPHFaceRecognizer()
    recognizer.load('trainer/trainer.yml')
    cascadePath = "/home/nicole/opencv-3.2.0/data/haarcascades/haarcascade_frontalface_alt.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);
    font = cv2.FONT_HERSHEY_SIMPLEX
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
            if Id != 'Unknow':
                print(Id,file=outfile)
                outfile.close()
                today = datetime.date.today()
                cam.read()
                camera_capture = get_image(cam)
                file = str(today.year) + str(today.month) + str(today.day) + '.png'
                cv2.imwrite(file, camera_capture)
                anchor = 1
                break
        if anchor == 1:
            cv2.destroyAllWindows()
            break
        
        # Display the video frame with the bounded rectangle
        cv2.imshow('im',im) 

        # If 'q' is pressed, close program
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    # Stop the camera
    #cam.release()

    # Close all windows
    #cv2.destroyAllWindows()

# Captures a single image from the camera and returns it in PIL format 
def get_image(camera):
    # read is the easiest way to get a full image out of a VideoCapture object.
    retval, im = camera.read()
    return im
def analysis(camera):
    print('analying')
    output1 = os.popen('alpr ./car.png')
    output = output1.read()
    print("1:" + output)
    if str(output[:2]) != 'No':
        #del(camera)
        #cv2.destroyAllWindows()
        fname = "data.txt"
        outfile = open(fname, "w")
        print( output[25:32],file=outfile)
        #print( 'ggggggg',file=outfile)
        time.sleep(2)
        face(camera,outfile)
        output1 = os.popen("rsync -av --delete -e 'ssh -p 3261' car.png nicole@ms15.voip.edu.tw:/home/project/104/nicole/www/LSA")
        output1 = os.popen("rsync -av --delete -e 'ssh -p 3261' 2018117.png nicole@ms15.voip.edu.tw:/home/project/104/nicole/www/LSA")
        output1 = os.popen("rsync -av --delete -e 'ssh -p 3261' data.txt nicole@ms15.voip.edu.tw:/home/project/104/nicole/www/LSA")
        #os.popen('python face_recognition.py')
        #sys.exit()
def main():
    i=0
 # Camera 0 is the integrated web cam on my netbook
    camera_port = 0

 #Number of frames to throw away while the camera adjusts to light levels
    ramp_frames = 30

 # Now we can initialize the camera capture object with the cv2.VideoCapture class.
 # All it needs is the index to a camera port.
    camera = cv2.VideoCapture(camera_port)

 # Ramp the camera - these frames will be discarded and are only used to allow v4l2
 # to adjust light levels, if necessary
# for i in range(ramp_frames):
#  temp = get_image(camera)
    while(True):

        camera.read()
        if (i%10==0): 
            print("Taking image...")
   # Take the actual image we want to keep
            camera_capture = get_image(camera)
   #cv2.imshow('frame',camera_capture)
            file = "car.png"
   # Display the resulting frame
   #cv2.imshow('frame',camera_capture)

   # A nice feature of the imwrite method is that it will automatically choose the
   # correct format based on the file extension you provide. Convenient!
            cv2.imwrite(file, camera_capture)

   # You'll want to release the camera, otherwise you won't be able to create a new
   # capture object until your script exits 
            analysis(camera)  
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            time.sleep(1)
        i+=1
    del(camera)
    cv2.destroyAllWindows()
main()
