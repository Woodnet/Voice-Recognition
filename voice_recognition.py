import speech_recognition as sr
import sys,os

def s_p(nachricht):
    sys.stdout.write("\r %s"%(nachricht))
    sys.stdout.flush()

daten = {
    'files':[
        "datei_1.wav", 
        "datei_2.wav",
    ],
}

if __name__ == '__main__':
    os.system("cls") #Windows -default
    zähler = 0
    for file in daten['files']:
        z = zähler
        z += 1
        s_p("INFO: Number: %s | File: %s.."%(z,file))
        r = sr.Recognizer()
        file = sr.AudioFile(file)
        with file as source:
            audio = r.record(source)
        print(" (+) Success")
        print(" (#) File-Content:\n %s\n"%(r.recognize_google(audio)))
        zähler += 1
    print("\n")
    n = input(">>> ")
