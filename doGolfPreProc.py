

def createImages(fila,pos):
    ''' 
    Given a video file location (fila) it will save as images to a folder
    Given positions in video (pos) these images from the video are saved
    pos is created based on positions of swings
    '''
    import cv2
    import numpy as np
    import os
    
    # create a video capture object
    cap = cv2.VideoCapture(fila)
    
    # get details of the video clip
    duration = cap.get(cv2.CAP_PROP_POS_MSEC)
    
    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    duration_seconds = frame_count / fps
    print('duration is ',duration,'. frame_count is ',frame_count,'. fps is ',fps,'. duration sec is',duration_seconds)
    
    #alter pos based on frame count
    posb4=pos
    pos=(pos/(np.max(pos)/frame_count))
    pos=np.array([int(nn) for nn in pos])
    pos=pos[1:-2]#ignore first value and last two
    
    
    # create a folder if it doesn't exist
    folder = fila.split('\\')[-1].split('.')[0]
    folder = '_images'+folder
    print(folder)
    try:
        os.mkdir(folder)
    except:
        pass

    
    vidcap = cap
    
    # this function creates an image from part of a video and 
    # saves as a JPG file
    def getFrame(sec,go):
        vidcap.set(cv2.CAP_PROP_POS_MSEC,sec)
        hasFrames,image = vidcap.read()
        if hasFrames and go:
            cv2.imwrite(os.path.join(folder,"frame{:d}.jpg".format(count)), image)     # save frame as JPG file
        return hasFrames
    
    # goes through the video clip and steps through based on frame rate
    sec = 0
    frameRate = 1000/fps 
    count=1
    go=0
    success = True
    while success:
        count = count + 1
        sec = sec + frameRate
        #only saves images if at positions in pos
        if count in pos:
            go=1
        else:
            go=0
        success = getFrame(sec,go)

    print("{} images are extacted in {}.".format(count,folder))
    
    
