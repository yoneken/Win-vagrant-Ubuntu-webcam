import cv2
import skvideo.io
import sys, argparse

def process(cap):
    while True:
        try:
            if isinstance(cap, type(cv2.VideoCapture())): 
                ret, frame = cap.read()
            else:
                frame = next(cap)
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            cv2.imshow('cap', frame)

            key = cv2.waitKey(1)
            if key == 27: # ESC
                cv2.imwrite('/webcam_test/cap.jpg', frame)
                break

        except:
            print(sys.exc_info())
            break


def process_camera(dev_num: int = 0) -> int:
    cap = cv2.VideoCapture(dev_num)

    process(cap)

    cap.release()
    cv2.destroyAllWindows()
    return 0

def process_video(filename) -> int:
    cap = skvideo.io.vreader(filename)

    process(cap)

    cv2.destroyAllWindows()
    return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='camera app')
    parser.add_argument('--input', '-i', type=str, default='0', help='Device number or a video file')
    args = parser.parse_args()

    if len(sys.argv) == 1:
        process_camera()
    elif args.input.isdecimal():
        process_camera(int(args.input))
    else:
        process_video(args.input)
