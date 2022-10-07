import qrcode

#첫번째 예제
QR = qrcode.QRCode()

QR.add_data("\\이승현,서울특별시,22살,군필")
Gen_Qr = QR.make_image(fill_color = "red", black_color = "black")
Gen_Qr.save('shl.jpg')
#img.save("test.jpg")
#print(type(img))
#print(img.size)