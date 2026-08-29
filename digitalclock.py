import tkinter as tk
from time import strftime

root=tk.Tk()
root.title("Digital Clock")
root.geometry("500x200")

def update_time():
    current_time=strftime("%H:%M:%S %p")
    clock_label.config(text=current_time)
    clock_label.after(1000,update_time)
    
clock_label=tk.Label(
    root,
    font=("Arial",80),
    background="black",
    foreground="white"
    
)

clock_label.pack(expand=True,fill="both")
update_time()

root.mainloop()