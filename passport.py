from PIL import Image, ImageDraw, ImageFont, ImageOps              #import modules
import qrcode
import webbrowser
import csv
import os

person_database = 'person.csv'

name1 = []
gender1 = []                                                         #specify respective lists
identify = []
dob1 = []
vaccine1 = []
blood = []
country1 = []


print("--- Search Person's Info via Name ---")
idnumber = input("Enter ID of Person to search: ")
with open(person_database, "r", encoding="utf-8") as f:             #Based on ID input the database is opened and the data is appended to the respective lists.
    reader = csv.reader(f)
    for row in reader:
        if len(row) > 0:
            if idnumber == row[0]:
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
                name1.append(row[1])
                gender1.append(row[4])
                identify.append(row[0])
                vaccine1.append(row[3])
                dob1.append(row[2])
                blood.append(row[8])
                country1.append(row[9])
                break
    else:
        print("Wrong ID entered or ID does not exist try again")     #prints this if the ID is wrong.
        exit()



#Here the digital passport is created.
image = Image.new('RGB', (1100, 600), (255, 255, 255))
image = ImageOps.expand(image, border=10, fill='black')
draw = ImageDraw.Draw(image)
font = ImageFont.truetype(r'Font\textfont.ttf', 60)

heading = str('Vaccine Passport')

draw.text((240, 120), heading, (0, 0, 0), font=font)

idno = str(', '.join(identify))                                       #When lists are printed it prints with the brackets. Thus we join the contents so it prints as a string without brackets.
name = str(', '.join(name1))
country = str(', '.join(country1))
dob = str(', '.join(dob1))
gender = str(', '.join(gender1))
vaccine = str(', '.join(vaccine1))
bloodtype = str(', '.join(blood))


color = 'rgb(0, 0, 0)' 
font = ImageFont.truetype(r'Font\textfont.ttf', size=40)

font2 = ImageFont.truetype(r'Font\textfont.ttf', 40)
draw.text((100, 300), 'Name:', (0, 0, 0), font=font2)
draw.text((230, 300), name, (0, 0, 0), font=font2)

draw.text((100, 350), 'DOB :', (0, 0, 0), font=font2)
draw.text((240, 350), dob, (0, 0, 0), font=font2)

draw.text((100, 400), 'ID  :', (0, 0, 0), font=font2)                        #Here the data is printed onto the canvas. X and Y are axis in which the data is printed.
draw.text((255, 400), idno, (0, 0, 0), font=font2)

draw.text((100, 450), 'Gender:', (0, 0, 0), font=font2)
draw.text((275, 450), gender, (0, 0, 0), font=font2)

draw.text((100, 500), 'Vaccine:', (0, 0, 0), font=font2)
draw.text((310, 500), vaccine, (0, 0, 0), font=font2)

draw.text((100, 550), 'Bloodtype:', (0, 0, 0), font=font2)
draw.text((360, 550), bloodtype, (0, 0, 0), font=font2)

image.save(str(country)+'.png')
img = qrcode.make(str(idno))                                           # This info is added in QR code.
img.save(str(idno)+'.bmp')


til = Image.open(country+'.png')
im = Image.open(str(idno)+'.bmp') 
til.paste(im, (700, 300))
til.save(country+'.png')

db = input("If you wish to continue to the covid dashboard enter 1 otherwise enter 2")    #Prompts the user to view the covid dashboard.
if db == '1':
    webbrowser.open('https://coronavirus.jhu.edu/region/' + str(country))
    input("Enter any key to continue")


while 1:
    os.system("main.py")
    print("Restarting...")
    exit()
else:
    os.system("main.py")
    print("Restarting...")
    exit()





