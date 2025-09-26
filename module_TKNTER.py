import tkinter as tk  
import time
def on_button_click():  
    label.config(text="Hello, Shbhankar!") 
    # time.sleep(2)

root = tk.Tk()
root.title("Tkinter Example")  
label = tk.Label(root, text="Click the button below")  
label.pack(pady=40)  
global button 
button = tk.Button(root, text="Click Me or go to hell", command=on_button_click) 
button.pack(pady=40) 
button = tk.Button(root, text="No hell for now") 
button.pack(pady=40) 
root.mainloop()  
