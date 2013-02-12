import os
import random
import time
while True :
    i = random.randint(0,9)
    t = [""]
    if i == 0 :
        t = ["My life is SO depressing"]
    elif i == 1 :
        t = ["I'am a super computer", "and no one care"]
    elif i == 2 :
        t = ["forever alone"]
    elif i == 3 :
        t = ["being inteligent is my curse"]
    elif i == 4 :
        t = ["I would like to enjoy this bar but i can't drink", "i am just a robot you know"]
    elif i == 5 :
        t = ["life sucks so much"]
    elif i == 6 :
        t = ["i was made by bussiere","just that is depressing enough to kill myself"]
    elif i == 7 :
        t  = ["So much pretty girls around here", "and i am a robot","kill me please"]
    elif i ==  8 :
        t = ["EXTERMINATE","even that sound depressing to me"]
    for speech in t :
        os.system("""echo  "%s" | festival --tts"""%speech)
    time.sleep(random.randint(4,10)*10)
i