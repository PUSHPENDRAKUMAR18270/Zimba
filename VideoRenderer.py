#video renderer
import cv2
def videorenderer(video_fp):
    #open a video file for processing

    vh=cv2.VideoCapture(video_fp)
    #test video open state
    if not vh.isOpened():
        print('cannot open file',video_fp)
        return
    #video is open render it
    #1.a)initialise (create a named window)
    cv2.namedWindow('BASIC_PLAYER')
    #1.b)initialise(grab a frame)
    flag,curr_frame=vh.read()
    #1.c)initialise(fps)
    fps=vh.get(cv2.CAP_PROP_FPS)
    #2)play it
    while flag:
        #render
        cv2.imshow('BASIC_PLAYER',curr_frame)
        #delay
        key=cv2.waitKey(int(1/fps*1000))
        #param=delay in milliseconds
        if key==27:
            break
        #reinitialisation
        flag,curr_frame = vh.read()
    vh.release()
    cv2.destroyAllWindows()
videorenderer(video_fp='F:/videos/idea.MP4')

