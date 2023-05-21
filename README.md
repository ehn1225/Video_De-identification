<h2>Video_De-identification</h2>
<p>
이 프로그램은 Python과 OpenCV, YOLO를 이용하여 만든 개인 비식별화 프로그램입니다.<br>
동영상에서 사람을 식별하고 모자이크를 적용함으로써 개인정보를 보호할 수 있습니다.<br>
</p>

<h2>Preparation</h2>
이 프로그램을 사용하기 위해서 python과 OpenCV가 필요합니다.
<p>pip install opencv-python opencv-contrib-python</p>
추가적으로, YOLO를 사용하기 위해서는 YOLO의 yolov3.cfg, yolov3.weights, coco.names 파일이 필요합니다. 아래 링크에서 다운로드 가능합니다.<br>
<p>yolov3.cfg, yolov3.weights : https://pjreddie.com/darknet/yolo/</p>
<p>coco.names : https://github.com/pjreddie/darknet/blob/master/data/coco.names</p>

<h2>기능</h2>
사람 비식별화(모자이크 처리), 모자이크 처리된 영상 저장<br>

<h2>Reference</h2>
https://yeko90.tistory.com/entry/opencv-yolov3-사용-방법
https://pjreddie.com/darknet/yolo/
https://github.com/pjreddie/darknet/blob/master/data/coco.names