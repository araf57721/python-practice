# m = []
# n = int(input(" Enter iteration number : "))
# for i in range(n):
#     v = float(input("Enter "+ str(i+1) +" value : "))
#     m.append(v)
# m.sort()
# print(m)

# c = int(len(m)/2)
# if(len(m)%2 == 0):
#     f = float((m[c] + m[c-1])/2)
#     print(f)

# else:
#     print(m[c])

import customtkinter as ctk
from tkinter import messagebox
import random
app = ctk.CTk()
app.geometry("1400x750")

app.title("My first page")
app.configure(fg_color = "red")

frame = ctk.CTkFrame(app, fg_color= "#874BC3")
frame.pack(fill = "both", expand = True)

l1 = ctk.CTkLabel(frame, text= "Welcome", text_color= "white", font=("Algerian", 40))
l1.pack(pady = 20)
l2 = ctk.CTkLabel(frame, text= "Can you love me ? ", text_color= "white", font=("Algerian", 40))
l2.pack(pady = 50)

def thank():
    messagebox.showinfo("Message", "I know that you love me ," + "\n" + "thank you.")

def move(event):
    o = random.randint(100, 1100)
    t = random.randint(100, 600)
    b2.place(x = o, y = t)



b1 = ctk.CTkButton(frame, text= "Yes", text_color= "red", font=("Algerian", 40), command= thank)
#b1.pack(pady = 40)
b1.place(x = 300, y = 260)
b2 = ctk.CTkButton(frame, text= "No", text_color= "black", font=("Algerian", 40))
#b2.pack(pady = 40)
b2.place(x = 850, y =260)
b2.bind("<Enter>", move)


app.mainloop()