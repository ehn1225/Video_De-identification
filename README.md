## Video_De-identification
이 프로그램은 Python과 OpenCV, YOLO를 이용하여 만든 개인 비식별화 프로그램입니다.   
동영상에서 사람을 식별하고 모자이크를 적용함으로써 개인정보를 보호할 수 있습니다.

## Preparation
#### 이 프로그램을 사용하기 위해서 python과 OpenCV가 필요합니다.   
- pip install opencv-python opencv-contrib-python   
#### 추가적으로, YOLO를 사용하기 위해서는 YOLO의 yolov3.cfg, yolov3.weights, coco.names 파일이 필요합니다.
- yolov3.cfg, yolov3.weights : https://pjreddie.com/darknet/yolo/
- coco.names : https://github.com/pjreddie/darknet/blob/master/data/coco.names

## 기능
- 사람 비식별화(모자이크 처리), 모자이크 처리된 영상 저장

## 실행 화면
<img src="https://github.com/ehn1225/Video_De-identification/assets/5174517/29403668-1e0e-4b2e-98ca-f798f227ee31" width="642" height="752">

## Reference
- https://yeko90.tistory.com/entry/opencv-yolov3-사용-방법
- https://pjreddie.com/darknet/yolo/
- https://github.com/pjreddie/darknet/blob/master/data/coco.names
- https://pixabay.com/ko/videos/
