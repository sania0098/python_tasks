# import cv2
# import numpy as np
# import pytesseract
#
#
# pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#
# cascade= cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
# states={"AN":"Andamam and Nicobar","AP":"Andhra Pradesh","AS":"AS",
#         "CH":"Chandigarh","DN":"Dadra and Nagar Haveli","DD":"Daman and Diu","DL":"Delhi",
#         "HR":"Haryana","HP":"Himachal Pradesh","JK":"Jammu and Kashmir","KA":"karnataka",
#         "MP":"Madhya Pradesh","PN":"Punjab","RJ":"Rajasthan",
#         "WB":"West Bengal","CG":"Chhattisgarh","TS":"Telangana"}
#
# def extract_num(imp_name):
#         global read
#         img = cv2.imread(imp_name)
#         gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#         numberplate= cascade.detectMultiScale(gray,1.1,4)
#         for(x,y,w,h) in numberplate:
#                 a,b,= (int(0.02*img.shape[0]), int(0.258*img.shape[1]))
#                 plate=img[y+a:y+h-a, x+b:x+w-b, :]
#                 kernel= np.ones((1,1),np.uint8)
#                 plate=cv2.dilate(plate, kernel, iterations=1)
#                 plate = cv2.erode(plate, kernel, iterations=1)
#
#                 plate_gray=cv2.cvtColor(plate,cv2.COLOR_BGR2GRAY)
#                 (thresh,plate)=cv2.threshold(plate_gray, 127,255,cv2.THRESH_BINARY)
#                 read=pytesseract.image_to_string(plate)
#                 read=''.join(e for e in read if e.isalnum())
#                 stat=read[0:2]
#                 try:
#                         print("car Belongs to ",states[stat])
#                 except:
#                         print("State not recognised!!")
#                 print(read)
#                 cv2.rectangle(img,(x,y),(x+w, y+h),(51,51,255),2)
#                 cv2.rectangle(img, (x, y-40), (x + w, y ), (51, 51, 255))
#                 cv2.putText(img,read, (x,y-10),cv2.FONT_HERSHEY_SIMPLEX)
#                 cv2.imshow('PLate',plate)
#         cv2.imshow("Result", img)
#         cv2.imwrite('result.jpg',img)
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()
#
# extract_num('car_10.jpg')
#
#
#
#
#
#
import cv2
import numpy as np
import pytesseract

# Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the cascade classifier for Russian number plates
cascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")

# Dictionary of states
states = {"AN": "Andaman and Nicobar", "AP": "Andhra Pradesh", "AS": "Assam",
          "CH": "Chandigarh", "DN": "Dadra and Nagar Haveli", "DD": "Daman and Diu", "DL": "Delhi",
          "HR": "Haryana", "HP": "Himachal Pradesh", "JK": "Jammu and Kashmir", "KA": "Karnataka",
          "MP": "Madhya Pradesh", "PN": "Punjab", "RJ": "Rajasthan",
          "WB": "West Bengal", "CG": "Chhattisgarh", "TS": "Telangana"}


def extract_num(img_name):
    global read
    img = cv2.imread(img_name)
    if img is None:
        print("Error: Image not found or unable to open.")
        return

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberplates = cascade.detectMultiScale(gray, 1.1, 4)

    if len(numberplates) == 0:
        print("No number plate detected.")
        return

    for (x, y, w, h) in numberplates:
        a, b = (int(0.02 * img.shape[0]), int(0.258 * img.shape[1]))
        plate = img[y + a:y + h - a, x + b:x + w - b]

        if plate.size == 0:
            continue

        kernel = np.ones((1, 1), np.uint8)
        plate = cv2.dilate(plate, kernel, iterations=1)
        plate = cv2.erode(plate, kernel, iterations=1)

        plate_gray = cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY)
        (thresh, plate) = cv2.threshold(plate_gray, 127, 255, cv2.THRESH_BINARY)

        read = pytesseract.image_to_string(plate)
        print(read)
        read = ''.join(e for e in read if e.isalnum())
        stat = read[0:2]

        try:
            print("Car belongs to", states[stat])
        except KeyError:
            print("State not recognized!!")

        print(read)
        cv2.rectangle(img, (x, y), (x + w, y + h), (51, 51, 255), 2)
        cv2.rectangle(img, (x, y - 40), (x + w, y), (51, 51, 255), -1)

        cv2.putText(img, read, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

        cv2.imshow('Plate', plate)

    cv2.imshow("Result", img)
    cv2.imwrite('result.jpg', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


extract_num('car_9.jpg')