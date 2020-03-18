# fetching window frame properties
import cv2

# open a video file for processing
video_fp = 'F:/videos/idea.MP4'
vh = cv2.VideoCapture(video_fp)
if vh.isOpened():
    print('Frame width:', vh.get(cv2.CAP_PROP_FRAME_WIDTH))
    print('Frame height:', vh.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print('Frame count:', vh.get(cv2.CAP_PROP_FRAME_COUNT))
    print('frames per second:', vh.get(cv2.CAP_PROP_FPS))
    # release the resource
    vh.release()
else:
    print('cannot Open', video_fp)
