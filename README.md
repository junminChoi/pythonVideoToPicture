# pythonVideoToPicture 


### 프로그램 목적
----------------------------------------
영상에서 움직이는 물체가 있는지 판별합니다.
특정 거리 및 특정 범위 이상의 움직임이 없는경우, 시간.jpg파일로 사진을 캡쳐하여 저장합니다.
이는 웹캠 또는 카메라와 연결하여 실시간으로 동작을 멈출 경우 사진을 촬영하도록 하여 타이머 시간에 맞출 필요없는 타이머 촬영기를 구현하고자 하였습니다.


### 과제 내용
-------------------------------------
##### -BackgroundSubtractorKNN
배경 영상과, 움직이는 물체를 분리<br>
![backgroundsubtractorKNN](https://user-images.githubusercontent.com/75197352/170498976-40a41eb9-53aa-47a2-8490-147a441afe33.jpg)
##### -findContours
물체의 외곽선의 갯수를 리턴<br>
![findcontours1](https://user-images.githubusercontent.com/75197352/170498986-ff5b552f-267a-4094-9a05-8c2eaca931bf.jpg)
![findcontours2](https://user-images.githubusercontent.com/75197352/170498989-e6b8a877-3a64-46a2-8101-90863ca5f7c2.jpg)
##### -영상 가공
BackgroundSubtractorKNN을 이용해 분리된 영상에서 즉시 conturs를 찾게되면 외곽선의 갯수가 무수히 많아짐으로 연산속도가 낮아짐.
![영상바로contour](https://user-images.githubusercontent.com/75197352/170498994-65717f21-9003-45df-8561-ae616b0d9626.png)
>> 이미지 블러링 및 침식 기법을 통해 contures를 줄이고, 이진화하여 외곽선의 갯수를 더 확실하게 리턴받을 수 있게 됨.
>> ![블러링침식후](https://user-images.githubusercontent.com/75197352/170498992-7321a258-7465-4685-9877-4ed396ea9f3d.png)
>> ![이진화후](https://user-images.githubusercontent.com/75197352/170498998-e28d4f5b-a40e-486f-918e-d0244791ee97.png)


### 결과 영상
-------------------------------------
PPT 첨부 (page3)



