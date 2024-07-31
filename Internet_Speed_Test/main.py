from tkinter import * 
import speedtest
import threading

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    download = str(round(sp.download()/(10**6),3))+" Mbps"
    upload = str(round(sp.upload()/(10**6),3))+" Mbps"
    lab_down.configure(text=download)
    lab_up.configure(text=upload)

def start_speedcheck():
    threading.Thread(target=speedcheck).start()

sp = Tk()

sp.title(" Internet Speed Test ")
sp.geometry("500x650")
sp.configure(bg="dodgerblue")

lab = Label(sp,text = " Internet Speed Test ", font=("Helvetica", 30, "bold"), bg="dodgerblue", fg="white")
lab.place(x = 60 , y = 40, height = 50, width = 380)

lab = Label(sp,text = " Downloading Speed ", font=("Helvetica", 30, "bold"))
lab.place(x = 60 , y = 130, height = 50, width = 380)

lab_down = Label(sp,text = " 00 ", font=("Helvetica", 30, "bold"))
lab_down.place(x = 60 , y = 200, height = 50, width = 380)

lab = Label(sp,text = " Uploading Speed ", font=("Helvetica", 30, "bold"))
lab.place(x = 60 , y = 290, height = 50, width = 380)

lab_up = Label(sp,text = " 00 ", font=("Helvetica", 30, "bold"))
lab_up.place(x = 60 , y = 350, height = 50, width = 380)

button = Button(sp,text="CHECK SPEED",font=("Helvetica", 15, "bold"),relief = RAISED, bg="black", fg="azure", command = start_speedcheck)
button.place(x = 60 , y = 460, height = 50, width = 380)

sp.mainloop()