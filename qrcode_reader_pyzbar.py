import cv2
import pyzbar.pyzbar as pyzbar
import openpyxl
import xlrd
import pandas as pd
import qrcode
import pprint

def qrcreator(filename):

    QR = qrcode.QRCode()


    wb = openpyxl.load_workbook(filename)
    ws = wb.active



    for i in range(1,10):
        QR.clear()
        for row in ws[i]:
            print(row.value) #행의 값을 출력
            QR.add_data(row.value) #행의 값을 QR에 추가
            QR.add_data(",")#콤마를 이용하여 값을 구분해주기
        Gen_Qr = QR.make_image(fill_color = "black", back_color = "white")#QR코드를 만들어내는 make_image// fill_color -> 채우기 색, back_color -> 배경색
        Gen_Qr.save("qr{}.jpg".format(i))

def qrcode_receive():
    
    used_codes = [] #->파일에서 불러온 데이터를 받을 목적
    data_list = [] #->파일에서 데이터를 불러오기 위한 목적

    #try,except문을 이용하여 기존에 있는 파일을 열고, 데이터를 불러온다.(추후에 데이터가 없으면 추가하고, 아니면 추가하지 않기위한 과정)
    try:
        f = open("hello.txt", "r", encoding="utf8")
        data_list = f.readlines()
    except FileNotFoundError:
        pass
    else:
        f.close()

    for i in data_list:
        used_codes.append(i.rstrip('\n')) #data_list에 있는 데이터에서 <ENTER>를 제외한 값을 used_codes에 대입하기 위하여 for 반복문을 이용함



    for i in range(1,10):
        img = cv2.imread("qr{}.jpg".format(i))
        img = cv2.resize(img, (0, 0), fx=0.385, fy=0.385) #resize(img,(가로,세로),가로사이즈 배수, 세로 사이즈 배수)
        qr = cv2.QRCodeDetector() #opencv 함수 중에 QRCodeDetector사용 
        data, box, straight_qrcode = qr.detectAndDecode(img) #detectAndDecode() 함수는 3개의 값을 리턴하며 QR코드를 리턴한 데이터, 이미지에서 위치를 담은 사각형 정보, 이미지에서 QR 코드에 해당하는 이미지를 잘라낸 이미지 데이터.
        if data:
            if data in used_codes:
                print("이미 등록한 정보입니다.")
        
            elif data not in used_codes:
                print('QR코드 데이터: {}'.format(data))

                lefttop = int(box[0][0][0]), int(box[0][0][1])
                rightbottom = int(box[0][2][0]), int(box[0][2][1])
                cv2.rectangle(img, lefttop, rightbottom, (0, 0, 255), 5)
                cv2.imshow('img', img)
                f2 = open("hello.txt", "a", encoding="utf8")
                f2.write(data+'\n')
                f2.close()

            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print("인식 오류!")

qrcreator('breast_cancer.xlsx')
qrcode_receive()
