from tkinter import *
window=Tk()

# add widgets here


window.title('Simple Interest Calculator')
window.geometry("500x400")
window.configure(bg='lightcyan')

def calculate_interest():
    p=float(principle.get())
    r=float(rate.get())
    t=float(time.get())
    i=(p*r*t)/100
    interest=round(i,2)
    result_label.destroy()
    message=Label(result_frame,text="Interest on Rs."+str(p)+" at rate of interest "+str(r)+"% for "+str(t)+" years is Rs."+str(interest), bg = "grey", font=("Calibri", 12), width=55)
    message.place(x=20 , y=40)
    message.pack()

app_label=Label(window, text="SIMPLE INTEREST CALCULATOR", fg = "black", bg = "lightcyan", font=("Calibri", 20),bd=5)
app_label.place(x=20, y=20)

p_label=Label(window, text="Your Principle Amount:", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
p_label.place(x=20, y=90)
principle=Entry(window, text="", bd=2, width=22)
principle.place(x=180, y=92)

r_label=Label(window, text="Your Rate of Interest:", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
r_label.place(x=20, y=140)
rate=Entry(window, text="", bd=2, width=22)
rate.place(x=180, y=142)

t_label=Label(window, text="Your Time Period:", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
t_label.place(x=20, y=185)
time=Entry(window, text="", bd=2, width=22)
time.place(x=180, y=187)

calculate_button = Button(window , text="Calculate" ,fg="black" , bg="lightcyan" , bd=4 , command= calculate_interest)
calculate_button.place(x=150 , y= 250)

result_frame = LabelFrame(window,text="Result", bg = "lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()

window.mainloop()