#video renderer with frame grab feature
import cv2
class VideoFrameGrabber:
    def __init__(self,src):

        #open a video for processing
        self.vh=cv2.VideoCapture(src)
        #test open state
        if not self.vh.isOpened():
            raise Exception ('cannot open video'+src)
        #fetch the rendering rate
        fps=self.vh.get(cv2.CAP_PROP_FPS)
        self.renderingRate=int(1/fps*1000)
        #a frame
        self.curr_frame=None
        #call back
    def mouse_event(self,event,x,y,flags,params):
            if event==cv2.EVENT_LBUTTONDOWN:
                cv2.imwrite('F:/images/grab.jpg',self.curr_frame)
            elif event==cv2.EVENT_RBUTTONDOWN:
                copy=cv2.cvtColor(self.curr_frame,cv2.COLOR_BGR2GRAY)
                cv2.imwrite('F:/images/grab_grey.jpg',copy)

    def play(self):
        #create a window
        cv2.namedWindow('BASIC_PLAYER')
        cv2.setMouseCallback('BASIC_PLAYER',self.mouse_event)
        #read a frame(initialisation
        flag,self.curr_frame=self.vh.read()
        while flag:
            #render
            cv2.imshow('BASIC_PLAYER',self.curr_frame)
            #wait
            key=cv2.waitKey(self.renderingRate)
            if key==27:
                break
            #reinitialise
            flag,self.curr_frame=self.vh.read()

    def _del_(self):
        self.vh.release()
        cv2.destroyAllWindows()

def main():
    obj=VideoFrameGrabber('F:/videos/idea.MP4')
    obj.play()
main()