# Before runnning this program make sure you have the 'SIH Dataset.csv' in the same folder in  which your program is running.
# To the 'SIH Dataset', in the last row add any current approaching time in the 'start time' column or else you might have to wait for  
# too long to see the program in execution. 
# For example, if your current time is '19:21' then add the time '19:23' in your dataset and save it and wait for 2 minutes.
import pandas as pd
# Source:   https://yometro.com/buses/dtc-bus-route-131A (consecutive busses leave at 10 min interval)

datas=pd.read_csv("SIH Dataset.csv")

import time
from win10toast import ToastNotifier   # check if the window's api problem still persists then use
                                        # 'from plyer import notification'

toast = ToastNotifier()

numbers=datas['Bus Number']
start_time=datas['First Bus']
end_time=datas['Last Bus']

def find_index(column,value_to_find):
    for i in range(0,len(column)):
        if column[i]==value_to_find:
            return i

while True:
    currTime=time.strftime("%H:%M")
    if currTime.startswith("0"):
        currTime = currTime[1:]
    else:
        currTime = currTime

    for i in start_time:
        if i==currTime:    # Near about same time k upr bhi ek optimised code likhna h
           # index=datas[datas['First Bus'] == i].index.tolist()
             index=find_index(start_time, i)
             toast.show_toast(
                f"Depart Bus Number {numbers[index]}",
                '''This will contain the details of the bus like Bus number plate,
                Driver id number, conductor number, from whhich gate it will deport and so on''',
                duration = 0,
                threaded = True,
                )
             if end_time.at[index]!=currTime:
                if ':' in currTime[0:2]:
                     min=currTime[2:]
                     if (int(min)<50) :
                         currTime=currTime[0:2] + str(int(min)+10)
                     else :
                         currTime=str(int(currTime[0:1])+1) + ':0' + str(int(min)-50)    
                else:
                     min=currTime[3:] 
                     if (int(min)<50):
                         currTime=currTime[0:3] + str(int(min)+10)
                     else:
                         currTime=str(int(currTime[0:2])+1) + ':0' + str(int(min)-50)

                start_time.at[index] = currTime       
                print(start_time[index])

             else:
                 numbers.pop(index)
                 start_time.pop(index)
                 end_time.pop(index)
             
