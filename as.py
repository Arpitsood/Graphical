import pywhatkit
import time

def add_sec(Time, add):
    
    Time[2] = (Time[2]+add)
    Time[1] = Time[1]+((Time[2])//60)
    Time[0] = Time[0]+((min)//60)
    
    Time[2]%=60
    Time[1]%=60
    Time[0]%=24

t = time.localtime()

hour = t.tm_hour
min = t.tm_min
sec = t.tm_sec

Time = [hour, min, sec]
add_sec(Time,10)
pywhatkit.sendwhatmsg_instantly('+919418351246', 'Hello!!', 11)
