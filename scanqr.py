import csv
import cv2 
import pyzbar.pyzbar as pyzbar
import time


font = cv2.FONT_HERSHEY_PLAIN
person_database = 'person.csv'                  
cap = cv2.VideoCapture(0)

#This function scans the qr code using a webcam.
def scanner():
    global person_database
    
    cap = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_PLAIN

while True:
    _, frame = cap.read()

    decodedObjects = pyzbar.decode(frame)                                     #The qr code is decoded and printed on screen.
    for obj in decodedObjects:
        cv2.putText(frame, str(obj.data), (10, 50), font, 2,
                    (255, 0, 0), 3)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

    for obj in decodedObjects:
        obj.data.decode('utf-8')                                   #When the data is decoded it is a byte meaning it will print with a b infront of it. To avoid this the data is converted to 8-Bit Universal Character Set Transformation Format ('utf-8')

        with open(person_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) > 0:
                    for obj in decodedObjects:
                        if obj.data.decode('utf-8') == row[0]:                #The data from the qr code is extracted and is scanned in the database. If the ID is found it prints the data.
                            print("----- Person Found -----")
                            print("ID: ", row[0])
                            print("Name: ", row[1])
                            print("Dob: ", row[2])
                            print("Vaccine: ", row[3])
                            print("Gender: ", row[4])
                            print("Address: ", row[5])
                            print("Batch Number: ", row[6])
                            print("Phone: ", row[7])
                            print("Blood Type: ", row[8])
                            print("Country: ", row[9])
                            time.sleep(2)
                            
                else:
                    pass
                




                        
