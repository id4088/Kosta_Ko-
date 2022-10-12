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
	cout << "��ĸ�� C��ư, �̹����� I��ư�� �����ֽñ� �ٶ��ϴ�.\n";
	cout << "����� Esc ��ư�� ��������.\n";
	int key;
	string qr;
	key = _getch();


	if (key == 105 || key == 73)
		qr = image();
	else if (key == 67 || key == 99)
		qr = camera();
	else if (key == 27)
		return;
	cout << "����" << qr << endl;
}
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
	cout << "�̹��� �̸��� �����ּ���(Ȯ���� ����)\n";
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
	//���� ����
	bool detctor_ok = false;//���� ���� ����
	string return_value;// qr�� ��ȯ
	int count = 0;//���� ������ ���� ī��Ʈ

	//ī�޶� �۵�
	VideoCapture cap(0);
	
	//���� ���н�
	if (!cap.isOpened()) {
		cerr << "Camera open failed! " << endl;
		return 0;
	}
	
	QRCodeDetector detector;//qr ���̺귯�� ȣ��
	
	Mat frame;//ī�޶� ������ ����
	//���� ����� ���� �ݺ���
	while (true) {
		
		cap >> frame;//ī�޶󿡼� �������� ���
		Mat frame2 = frame(Rect(225, 150, 200, 200));//frame���� ���� ����� ���� ����� frame2 ����
		//�������� ���� ���н� ���� ���
		if (frame.empty()) {
			cerr << "Frame load failed!" << endl;
			break;
		}

		vector<Point> points;//qr�� ��ǥ ����
		string info = detector.detectAndDecode(frame2, points);//frame2 ���� qr�� ����,info�� qr ���� �Է�,points�� ��ǥ �Է�
		
		//info�� ���빰 ������ �۵�
		if (info.empty()) {
			
			rectangle(frame, Rect(225, 150, 200, 200),
				Scalar(255, 255, 255), 2);//��� Ⱥ�� ���� ����
			
		}
		else if (!info.empty())
		{	
			rectangle(frame, Rect(225, 150, 200, 200),Scalar(0, 0, 255), 2);//���������� ����
			polylines(frame2, points, true, Scalar(0, 0, 255), 1);//qr�� ���� ���� ǥ��
			putText(frame, info, Point(10, 30), FONT_HERSHEY_DUPLEX, 1, Scalar(0, 0, 255));//qr ���� ȭ�� ���
			return_value = info;//�ݺ������� ���� �ʱ�ȭ�� ���Ͽ� ���ǼҸ� �����.
			detctor_ok = true; 
			
		}
		
		//�Լ� ���� ī��Ʈ �ٿ�
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
			
		//����Ű �Է½� ����
		if (waitKey(1) == 13)	
			break;
	}
}