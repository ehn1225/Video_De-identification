import cv2
import numpy as np

# YOLO 모델 로드
weights_path = "./yolov3.weights"
config_path = "./yolov3.cfg"
net = cv2.dnn.readNetFromDarknet(config_path, weights_path)

# COCO 데이터셋의 클래스 이름 파일 경로
names_path = "./coco.names"
with open(names_path, "r") as f:
    classes = [line.strip() for line in f.readlines()]

# YOLO 모델의 출력 레이어 가져오기
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# 동영상 로드
video_path = "./subway.mp4"
cap = cv2.VideoCapture(video_path)

# 동영상 출력 설정
output_path = "./output.avi"
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*"MJPG")
outvideo = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# 프레임 반복 처리
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 이미지 전처리
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    # 객체 감지 및 모자이크 처리
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > 0.5 and class_id == 0:  # 0은 '사람' 클래스에 해당
                # 객체의 경계 상자 좌표
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                if(x < 1):
                    x = 0
                if(y < 1):
                    y = 0
                if(y+h > height):
                    h = height - y
                if(x+w > width):
                    w = width - x

                # 모자이크 처리를 위한 사각형 그리기
                blur_image = frame[y:y+h, x:x+w]
                blur_image = cv2.GaussianBlur(blur_image, (5, 5), 30)

                # 모자이크 처리된 이미지로 대체
                frame[y:y+h, x:x+w] = blur_image 

    # 모자이크 처리된 프레임 저장
    outvideo.write(frame)

    # 화면에 출력
    cv2.imshow("Mosaic Result", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 해제
cap.release()
outvideo.release()
cv2.destroyAllWindows()
