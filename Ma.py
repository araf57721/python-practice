import customtkinter as ctk
from tkinter import messagebox
app = ctk.CTk()
app.title("My first app")
app.geometry("1400x700")
app.configure(fg_color = "orange")
frame1 = ctk.CTkFrame(app)
frame1.pack(fill = "both",expand = True)

# frame2 = ctk.CTkFrame(app)
# def next_app():
#     frame1.pack_forget()
#     frame2.pack(fill = "both", expand = True)

my_lebel = ctk.CTkLabel(frame1, text="Welcome", text_color = "#800080", font = ("Arial",28))
my_lebel.pack(pady =50)

entry1 = ctk.CTkEntry(frame1, width = 250, placeholder_text = "Enter Kg ")
entry1.pack()

entry2 = ctk.CTkEntry(frame1, width = 250, placeholder_text = "Enter height in feet", placeholder_text_color= "blue", font= ("Arial",20))
entry2.pack()

entry3 = ctk.CTkEntry(frame1,width=240,placeholder_text= "Enter height in inch", placeholder_text_color= "green", font= ("Arial",20))
entry3.pack()

entry4 = ctk.CTkEntry(frame1, width = 250, placeholder_text = "Result", placeholder_text_color= "gray")
entry4.pack(pady = 20)

def show_app():
    a = float(entry1.get())
    b = float(entry2.get())
    c = float(entry3.get())
    d = b* 0.3048
    e = c* 0.0254
    f = d+e
    g = f * f
    result = (a/g)

    entry4.delete(0,"end")
    entry4.insert(0,result)

    if(result < 18.5):
        str1 = "underweight"
        messagebox.showinfo("Message",str1)
    elif(result>=18.5 and result <= 24.9):
        str2 = "Good health"
        messagebox.showinfo("Message", str2)
    elif(result>=25 and result <= 29.9):
        str3 = "over weight"
        messagebox.showinfo("Message", str3) 
    else:
        str4 = "go to the hospital"
        messagebox.showinfo("Message",str4)

button1 = ctk.CTkButton(frame1, text = "Show BMI", text_color="orange", command=show_app)
button1.pack(pady = 10)

def exit_app():
    app.destroy()

button2 = ctk.CTkButton(frame1, text = "Exit", text_color="green", command= exit_app)
button2.pack(pady = 10)

frame2 = ctk.CTkFrame(app)
def next_app():
    frame1.pack_forget()
    frame2.pack(fill = "both", expand = True)


button3 = ctk.CTkButton(frame1, text= "Next",text_color= "yellow", command= next_app )
button3.pack(pady = 20)
app.mainloop()

