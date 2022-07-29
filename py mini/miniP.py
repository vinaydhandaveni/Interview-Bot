import speech_recognition as sr
import pyttsx3 
import os
import numpy as np
import cv2
import threading

def recvid(name):
 cap = cv2.VideoCapture(0)
 fourcc = cv2.VideoWriter_fourcc(*'XVID')
 out = cv2.VideoWriter("name.avi", fourcc, 20.0, (640, 480))
 while(True):
  ret, frame = cap.read()
  out.write(frame)
  #cv2.imshow('Original', frame)
  if cv2.waitKey(1) & 0xFF == ord('a'):
      break
 cap.release()
 out.release()
 cv2.destroyAllWindows()

def createdi(name):
    try:
        parent_dir = os.getcwd()
        new=parent_dir+"/"+name
        mode = 0o666
        path = os.path.join(parent_dir, name)
        os.mkdir(path, mode)
    except FileExistsError:
        print("Welcome again",name)
    os.chdir(new)

def record(name,qs) :
 #recvid(name)
 import speech_recognition as sr
 mic_name = sr.Microphone(device_index=1)
 sample_rate = 48000
 chunk_size = 2048
 r = sr.Recognizer()
 mic_list = sr.Microphone.list_microphone_names()
 device_id=1
 with sr.Microphone(device_index = device_id, sample_rate = sample_rate,chunk_size = chunk_size) as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)      
    try:
        text = r.recognize_google(audio)
        save(name,qs,text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
      
    except sr.RequestError as e:
        print("Could not request results from Google  Speech Recognition service; {0}".format(e))


def save(name,qsn,ans) :
    fp=open(name,'a')
    fp.write(qsn)
    fp.write(ans)
    fp.write("\n")
    fp.close()

def current(name):
    #createdi(name)
    #recvid(name)
    fp = open("currentaffairs.txt",'r')
    createdi(name)
    try:
        t1=threading.Thread(target=recvid,args=(name,))
        t1.start()
    except:
        print("cannot record")
    for item in fp :
     print(item)
     record(name,item)
    fp.close()

def GK(name):
    #createdi(name)
    #recvid(name)
    fp = open("GK.txt",'r')
    createdi(name)
    try:
        t1=threading.Thread(target=recvid,args=(name,))
        t1.start()
    except:
        print("cannot record")
    for item in fp :
     print(item)
     record(name,item)
    fp.close()

def programming(name):
    #createdi(name)
    #recvid(name)
    fp = open("programming.txt",'r')
    createdi(name)
    try:
        t1=threading.Thread(target=recvid,args=(name,))
        t1.start()
    except:
        print("cannot record")
    for item in fp :
     print(item)
     record(name,item)
    fp.close()

def verb(name):
    #createdi(name)
    #recvid(name)
    fp = open("Verbalability.txt",'r')
    createdi(name)
    try:
        t1=threading.Thread(target=recvid,args=(name,))
        t1.start()
    except:
        print("cannot record")
    for item in fp :
     print(item)
     record(name,item)
    fp.close()
print("\n\t\t---------Interview Bot-----------\n\n")
name  =  input("\nEnter your name : ")
mobyl =  input("\nEnter your mobile number  : ")
print("\nSelect the type of questions you want to select :")
print("\n1. current affairs\n2. General Knowlwdge\n3. programming\n4. Verbalability")
choice=int(input("\nyour choice : "))
if choice==1 :
   current(name)
elif choice==2 :
   GK(name)
elif choice==3 :
  programming(name)
elif choice==4 :
  verb(name)
else :
  print("wrong input")