import face_recognition
import cv2
import pymysql # from Lib folder
from datetime import datetime
from tkinter import messagebox

def detect(email):
   db = pymysql.connect("127.0.0.1","root","1234","test",3309)#sqlyog
   cursor = db.cursor()
   #initializing variables
   known_face_encodings=[]
   i=0
   images_Path=[]
   known_face_names = []
   known_face_id=[]
   sql = "SELECT * FROM students where email='%s'"%(email)
      # Execute the SQL command
   cursor.execute(sql)
      # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
         student_name = row[0]
         email = row[1]
         id = row[2]
         img_path=row[9]
      
         images_Path.append(row[9])
         known_face_names.append(row[0])
         known_face_id.append(row[2])
   for x in images_Path:
         print(x)
         my_image = face_recognition.load_image_file(x)
         my_face_encoding = face_recognition.face_encodings(my_image)[0]
         known_face_encodings.append(my_face_encoding)
 
         '''from datetime import date
         from datetime import time
         x = date.today()
         
         #print("Current Date= ",x)
         datee=x
         #print("Current Year= ",x.year)
         #print("Current Month= ",x.month)
         #print("Current Day= ",x.day)
         dayy=x.day
         x=datetime.today().strftime('%A')
         #print(x)
         now=datetime.now()
         timee=now.strftime("%H:%M")
         #print(now.strftime("%I:%M:%S:%p"))
        # print(now.strftime("%H:%M"))
         
      
     # Now print fetched result
         i=0
         sql="Insert into record values("+str(id)+",'"+str(name)+"','"+str(email)+"','"+str(timee)+"','"+str(dayy)+"','"+str(datee)+"')"
         i=cursor.execute(sql)
         db.commit()
      
         
   # disconnect from server
   db.close()
   if i>0:
      print((len(images_Path)))
   else:
      print ("Error: unable to fetch data")'''


   # Get a reference to webcam #0 (the default one)
   video_capture = cv2.VideoCapture(0)

   # Initialize some variables
   face_locations = []
   face_encodings = []
   face_names = []
   face_id=[]
   process_this_frame = True

   while True:
       # Grab a single frame of video
          ret, frame = video_capture.read()

       # Resize frame of video to 1/4 size for faster face recognition processing
          small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

       # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
          rgb_small_frame = small_frame[:, :, ::-1]

       # Only process every other frame of video to save time
          if process_this_frame:
           # Find all the faces and face encodings in the current frame of video
              face_locations = face_recognition.face_locations(rgb_small_frame)
              face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
              face_id=[]
              face_names = []
              for face_encoding in face_encodings:
               # See if the face is a match for the known face(s)
                  matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                  name = "Unknown"
                  ids="Unknown"
               # If a match was found in known_face_encodings, just use the first one.
                  if True in matches:
                      first_match_index = matches.index(True)
                      name = known_face_names[first_match_index]
                      ids=known_face_id[first_match_index]
                      print(name,ids)
                      i=1
                  face_names.append(name)
                  face_id.append(ids)
          process_this_frame = not process_this_frame

       # Display the results
          for (top, right, bottom, left), name in zip(face_locations, face_names):
           # Scale back up face locations since the frame we detected in was scaled to 1/4 size
              top *= 4
              right *= 4
              bottom *= 4
              left *= 4

           # Draw a box around the face
              cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

           # Draw a label with a name below the face
              cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
              font = cv2.FONT_HERSHEY_DUPLEX
              cv2.putText(frame, "Name: "+name+"\nId: "+str(ids), (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
              
       # Display the resulting image
          cv2.imshow('Video', frame)

       # Hit 'q' on the keyboard to quit!
          if cv2.waitKey(1) & 0xFF == ord('q') or i==1:
             video_capture.release()
             cv2.destroyAllWindows()
             return 1

   # Release handle to the webcam
   
