import cv2
import os
import time
# Captures a single image from the camera and returns it in PIL format 
def get_image(camera):
 # read is the easiest way to get a full image out of a VideoCapture object.
    retval, im = camera.read()
    return im
def analysis():
    print('analying')
    os.system('alpr ./test_image.png')
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

    #因為中間會有延遲,但每次只會讀一張frame,這樣中間延遲的frame就會讓我們的程式不夠real time,所以要把它讀完
      camera.read()
      if (i%10==0): #延遲用
          print("Taking image...")
          # Take the actual image we want to keep
          camera_capture = get_image(camera)
          #cv2.imshow('frame',camera_capture)
          file = "test_image.png"
          # Display the resulting frame
          #cv2.imshow('frame',camera_capture)

          # A nice feature of the imwrite method is that it will automatically choose the
          # correct format based on the file extension you provide. Convenient!
          cv2.imwrite(file, camera_capture)
          
          # You'll want to release the camera, otherwise you won't be able to create a new
          # capture object until your script exits 
          analysis()  
          if cv2.waitKey(1) & 0xFF == ord('q'):
              break
           #因為不知道怎麼結束程式,只好設一個sleep,不然程式關不掉
          time.sleep(1)
      i+=1 #延遲用
    del(camera)
    cv2.destroyAllWindows()
main()
