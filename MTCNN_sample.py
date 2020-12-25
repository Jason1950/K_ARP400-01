from mtcnn import MTCNN
import cv2
import time

def initMTCNN():
    detector = MTCNN()
    return detector
def markKeyPoint(detector, image):
    result = detector.detect_faces(image)

    if len(result) > 0 :
        bounding_box = result[0]['box']
        keypoints = result[0]['keypoints']
        cv2.rectangle(image,
                    (bounding_box[0], bounding_box[1]),
                    (bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),
                    (0,155,255),
                    2)

        cv2.circle(image,(keypoints['left_eye']), 2, (0,155,255), 2)
        cv2.circle(image,(keypoints['right_eye']), 2, (0,155,255), 2)
        cv2.circle(image,(keypoints['nose']), 2, (0,155,255), 2)
        cv2.circle(image,(keypoints['mouth_left']), 2, (0,155,255), 2)
        cv2.circle(image,(keypoints['mouth_right']), 2, (0,155,255), 2)
    # image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    return image

ii = 0
# 選擇第二隻攝影機
cap = cv2.VideoCapture(0)
detector = initMTCNN()
# detector = MTCNN()

while(True):
    # 從攝影機擷取一張影像
    ret, frame = cap.read()
    
    if ret:
        time1 = time.time()
        frame = markKeyPoint(detector, frame)
        # 顯示圖片
        cv2.imshow('frame', frame)
        ii += 1
        print(f'fps : {round(1/(time.time()-time1),1)} ,the {ii} frame')
        
        # 若按下 q 鍵則離開迴圈
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print('False')

# 釋放攝影機
cap.release()

# 關閉所有 OpenCV 視窗
cv2.destroyAllWindows()
