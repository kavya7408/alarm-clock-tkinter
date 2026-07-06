import tkinter as tk
import winsound
from tkinter import messagebox
from tkinter import *
from datetime import datetime,timedelta
root = tk.Tk()
root.geometry("600x500")
root.title("Alarm clock")
root.config(bg="#F0F8FF")
alarms = []
def add_alarm():
    alarm = alarm_time.get()
    try:
        datetime.strptime(alarm, "%H:%M:%S")
        alarms.append(alarm)
        alarm_listbox.insert(tk.END, alarm)
        alarm_time.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Invalid Time","Use HH:MM:SS format")
def check_alarm():
    current_time = datetime.now().strftime("%H:%M:%S")
    if current_time in alarms:
        winsound.Beep(1000, 1000)
        messagebox.showinfo("Alarm", "wake up!")
        alarms.remove(current_time)
        index = alarm_listbox.get(0,tk.END).index(current_time)
        alarm_listbox.delete(index)
    else:
        root.after(1000,lambda: check_alarm())
def update_clock():
    current_time = datetime.now().strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    #this updates the time after every 1000 milliseconds
    root.after(1000,update_clock)
def update_date():
    current_date = datetime.now().strftime("%A,%d %B %Y")
    date_label.config(text=current_date)    
    root.after(1000, update_date)
def snooze_alarm():
    current_time = datetime.now()
    snooze_time = current_time + timedelta(minutes=5)
    alarms.append(snooze_time.strftime("%H:%M:%S"))
    alarm_listbox.insert(tk.END, snooze_time.strftime("%H:%M:%S"))
    winsound.PlaySound(None, winsound.SND_PURGE)
    messagebox.showinfo("Snoozed",f"Alarm postponed to {snooze_time.strftime('%H:%M:%S')}")
def delete_alarm():
    selected = alarm_listbox.curselection()
    if selected:
        index = selected[0]
        alarms.pop(index)
        alarm_listbox.delete(index)
label = tk.Label(root,text = "set alarm time")
label.pack(pady=10,padx=10)
alarm_time = tk.Entry(root,font=("Arial",20),width=15,justify="center")
alarm_time.pack(pady=10,padx=10)
date_label = tk.Label(root,font = ("Arial",20,"bold"),fg = "blue")
date_label.pack(pady=10,padx=10,side=TOP)
button_f = tk.Frame(root,bg="#F0F8FF")
button_f.pack(pady=10)
add_alarmb = tk.Button(button_f,text="add alarm",bg="#4CAF50",fg="white",font=("Arial",10,"bold"),command=add_alarm)
add_alarmb.pack(pady=10,side=BOTTOM)
del_b = tk.Button(button_f,text="delete alarm",bg="#4CAF50",fg="white",font=("Arial",10,"bold"),command = delete_alarm)
del_b.pack(pady=10,side=BOTTOM)
snooze_btn = tk.Button(button_f,text="Snooze 5 Min",bg="orange",fg="white",font=("Arial", 10, "bold"),command=snooze_alarm)
snooze_btn.pack(pady=5,side=BOTTOM)
heading=tk.Label(root,text="Scheduled alarms",bg="#4CAF50",fg="white",font=("Arial",20,"bold"))
heading.pack(padx=10,pady=5)
alarm_listbox = tk.Listbox(root,height=6,width=20,font=("Arial",14))
alarm_listbox.pack()
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
alarm_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=alarm_listbox.yview)
root.bind("<Return>",lambda event:add_alarm())
entry_button = tk.Button(button_f,text="start alarm",command=check_alarm,bg="#4CAF50",fg="white",font=("Arial",10,"bold"))
entry_button.pack(side=BOTTOM)
update_clock()
update_date()
check_alarm()
root.mainloop()