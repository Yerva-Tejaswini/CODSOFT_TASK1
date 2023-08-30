import tkinter as tk
def on_click(event):
    current_text=entry.get()
    button_text=event.widget.cget("text")

    if button_text=="=":
        try:
            result=eval(current_text)
            entry.delete(0,tk.END)
            entry.insert(tk.END,str(result))
        except Exception as e:
            entry.delete(0,tk.END)
            entry.insert(tk.END,"Error")
    elif button_text=="c":
        entry.delete(0,tk.END)
    elif button_text=="<-":
        current_text=entry.get()
        entry.delete(len(current_text)-1,tk.END)
    else:
        entry.insert(tk.END,button_text)

root=tk.Tk()
root.title("Calculator")

entry=tk.Entry(root,font=("Arial",30),justify="right",bg="black",fg="white")
entry.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

button_style={
    "font":("Arial",24),
    "padx":20,
    "pady":20,
    "width":3,
    "height":1,
    "borderwidth":2,
    "relief":tk.RAISED,
    "bg":"black",
    "fg":"white"
}

buttons=[
    ("1",2,0),("2",2,1),("3",2,2),("/",2,3),
    ("4",3,0),("5",3,1),("6",3,2),("*",3,3),
    ("7",4,0),("8",4,1),("9",4,2),("-",4,3),
    (".",5,0),("0",5,1),("+",5,2),("=",5,3),
    ("c",1,0),("(",1,1),(")",1,2),("<-",1,3)
]


for(button_text,row,column)in buttons:
    btn=tk.Button(root,text=button_text,**button_style)
    btn.grid(row=row,column=column,padx=5,pady=5)
    btn.bind("<Button-1>",on_click)


root.mainloop()