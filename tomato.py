import tkinter as tk
import math as m
import time
import threading
import winsound

def thread_it(func, *args):
    t = threading.Thread(target=func, args=args) 
    t.setDaemon(True)
    t.start()

def counttime():
    dotatime = float(entry.get()) 
    origintime = time.time()
    while True:
        nowtime = time.time()
        if (nowtime - origintime) <= 3000*dotatime:
            percent =(1-((nowtime - origintime) / (3000*dotatime)))*100
            label01.config(text="还有%.2f%%" % percent,)
        else:
            label01.config(text="完成")
            break
        time.sleep(0.5)
    winsound.PlaySound("dingdong.wav",flags=2)
    time.sleep(0.3)
    winsound.PlaySound("dingdong.wav",flags=2)
    time.sleep(0.3)
    winsound.PlaySound("dingdong.wav",flags=2)

window = tk.Tk()
window.title("My tomato")
window.geometry("150x120")
window.resizable(width=False, height=False)
label01=tk.Label(window,text="马上开始")
label02=tk.Label(window,text="时间")
botton=tk.Button(window,text="冲",command=lambda :thread_it(counttime))
entry=tk.Entry(window,font=('Arial', 12),width=4,highlightcolor='red',highlightthickness=1)
label01.pack()
label02.pack(side="left")
entry.pack(side="right")
botton.pack()
window.mainloop()