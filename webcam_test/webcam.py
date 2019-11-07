import cv2

def capture(device_no = 0):
    cap = cv2.VideoCapture(device_no)

    while True:
        ret, frame = cap.read()
        cv2.imshow('cap', frame)

        key = cv2.waitKey(1)
        if key == 27: # ESC
            cv2.imwrite('/webcam_test/cap.jpg', frame)
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture()