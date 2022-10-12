#include <opencv2/opencv.hpp>
#include <iostream>
#include <conio.h>
#include <time.h>

void qr_maun();

using namespace std;
using namespace cv;

void image2();
string camera();
string image();

int main(int argv, char** argc)
{
	
	qr_maun();
		 		
}
void qr_maun()
{
	cout << "윕캡은 C버튼, 이미지는 I버튼을 눌려주시기 바랍니다.\n";
	cout << "종료시 Esc 버튼을 누르세요.\n";
	int key;
	string qr;
	key = _getch();


	if (key == 105 || key == 73)
		qr = image();
	else if (key == 67 || key == 99)
		qr = camera();
	else if (key == 27)
		return;
	cout << "응답" << qr << endl;
}
//기울어진 qr 코드 인식 코드 실패!! 사용금지
void image2()
{
	Mat img = imread("qr2.jpg");
	//Mat mask = Mat::zeros(400, 600, CV_8U);
	Mat img2;
	resize(img, img, Size(600, 400));

	//circle(mask, Point(300, 200), 210, Scalar(255, 255, 255), -1);
	//IMREAD_GRAYSCALE

	//img.copyTo(img2, mask);
	//imshow("img2", img2);

	cvtColor(img, img2, COLOR_BGR2GRAY);

	edgePreservingFilter(img2, img2);
	GaussianBlur(img2, img2, Size(), (double)1);

	//imshow("img1", img);

	Canny(img2, img2, 50, 150);


	vector<vector<Point>> contours;
	findContours(img2, contours, RETR_EXTERNAL, CHAIN_APPROX_SIMPLE);
	drawContours(img, contours, 0, Scalar(0, 255, 0), 2);

	imshow("img2", img2);
	imshow("img1", img);	
	waitKey(0);
}
string image() {
	string img_name;
	cout << "이미지 이름을 적어주세요(확장자 포함)\n";
	cin >> img_name;

	Mat img = imread(img_name);
	
	QRCodeDetector detector;
	Mat img2;
	edgePreservingFilter(img, img2);

	Mat frame;
	vector<Point> points;
	String info = detector.detectAndDecode(img, points);
		
	if (!info.empty()) {

		polylines(img, points, true, Scalar(0, 0, 255), 1);

	}
	
	return info;
	
	waitKey(0);
		
}
string camera() {
	//변수 선언
	bool detctor_ok = false;//검출 유무 변수
	string return_value;// qr값 반환
	int count = 0;//검출 성공후 종료 카운트

	//카메라 작동
	VideoCapture cap(0);
	
	//실행 실패시
	if (!cap.isOpened()) {
		cerr << "Camera open failed! " << endl;
		return 0;
	}
	
	QRCodeDetector detector;//qr 라이브러리 호출
	
	Mat frame;//카메라 프라임 선언
	//영상 출력을 위한 반복문
	while (true) {
		
		cap >> frame;//카메라에서 프레임이 출력
		Mat frame2 = frame(Rect(225, 150, 200, 200));//frame에서 얇은 복사로 상자 모양의 frame2 생성
		//프레임이 제작 실패시 오류 출력
		if (frame.empty()) {
			cerr << "Frame load failed!" << endl;
			break;
		}

		vector<Point> points;//qr의 좌표 변수
		string info = detector.detectAndDecode(frame2, points);//frame2 영상에 qr을 검출,info에 qr 내용 입력,points에 좌표 입력
		
		//info의 내용물 유무로 작동
		if (info.empty()) {
			
			rectangle(frame, Rect(225, 150, 200, 200),
				Scalar(255, 255, 255), 2);//가운데 횐색 상자 형성
			
		}
		else if (!info.empty())
		{	
			rectangle(frame, Rect(225, 150, 200, 200),Scalar(0, 0, 255), 2);//빨간색으로 변경
			polylines(frame2, points, true, Scalar(0, 0, 255), 1);//qr에 빨간 상자 표시
			putText(frame, info, Point(10, 30), FONT_HERSHEY_DUPLEX, 1, Scalar(0, 0, 255));//qr 내용 화면 출력
			return_value = info;//반복문으로 인한 초기화로 인하여 대피소를 만든다.
			detctor_ok = true; 
			
		}
		
		//함수 종료 카운트 다운
		if (detctor_ok == true)
		{
			
			string ok_text = "detector ok";
			putText(frame, ok_text, Point(10, 60), FONT_HERSHEY_DUPLEX, 1, Scalar(0, 0, 255));
			count++;
			
		}
		
		
		imshow("frame", frame);
		
		if (count == 10)
		{
			destroyWindow("frame");
			return return_value;
			break;
		}
			
		//엔터키 입력시 종료
		if (waitKey(1) == 13)	
			break;
	}
}
