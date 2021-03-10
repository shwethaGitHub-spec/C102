import cv2
#https://pythonprogramming.net/loading-video-python-opencv-tutorial/#:~:text=VideoCapture(0)%20.,first%20webcam%20on%20your%20computer.&text=It%20is%20important%20to%20note,RGB%20(Red%20Green%20Blue).
def take_snapshot():
    #initializing cv2
    #VideoCapture(0) captures video from first webcam when it is 0
    videoCaptureObject = cv2.VideoCapture(0)
    result = True # booleans are written in starting letter cap letter(True , False)
    while(result):
        #read the frames while the camera is on
        
        #Basically, ret is a boolean regarding whether or not there was a return at all, 
        # at the frame is each frame that is returned.
        # If there is no frame, you wont get an error, you will get None.
        ret,frame = videoCaptureObject.read()
        
        #cv2.imwrite() method is used to save an image to any storage device
        cv2.imwrite("C102/NewPicture1.jpg",frame)
        result = False

    # releases the camera
    videoCaptureObject.release()
    #closes all the window that might be opened while this process
    cv2.destroyAllWindows()

take_snapshot()