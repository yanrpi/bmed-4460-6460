import argparse
import numpy as np
import cv2

# Background subtraction
def bgsub_demo(args):
    video_fn = args.f
    method = args.m
    
    cap = cv2.VideoCapture(video_fn)
    video_opened = cap.isOpened()
    if not video_opened:
        print('Video {} cannot be opened'.format(video_fn))
        return -1
    
    #length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if method == 0:
        print('Background subtraction with MOG')
        fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
    elif method == 1:
        # Background subtraction based on CNT method
        print('Background subtraction with CNT')
        fgbg = cv2.bgsegm.createBackgroundSubtractorCNT()
    elif method == 2:
        print('Background subtraction with GMG')
        fgbg = cv2.bgsegm.createBackgroundSubtractorGMG(15)
    else:
        print('Method can only be 0, 1 or 2!')
        return -2

    WINDOW_NAME = 'frame'
    cv2.namedWindow(WINDOW_NAME)

    # Play video only
    while(1):
        ret, frame = cap.read()
        if not ret:
            break
        height, width = frame.shape[:2]
        
        fgmask = fgbg.apply(frame)
        frame_concat = np.concatenate((frame[:,:,0], fgmask), axis=1)
        frame_concat = cv2.resize(frame_concat, (int(width*0.8), int(height*0.4)))
        cv2.imshow(WINDOW_NAME, frame_concat)

        k = cv2.waitKey(40) & 0xff
        if k == 27:
            break

    cv2.destroyAllWindows()
    cv2.waitKey(1)
    cap.release()

    
    
# Main file
if __name__ == '__main__':
    
    # Training settings
    parser = argparse.ArgumentParser(description='Demo background subtraction')
    parser.add_argument('-m', type=int, default=0, metavar='N',
                        help='method type [0, 1, or 2]')
    parser.add_argument('-f', type=str, default='10x_XY01_video_8bit.avi',
                        metavar='N',
                       help='video file name')    
    args = parser.parse_args()
    
    bgsub_demo(args)