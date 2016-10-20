try:
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    from tkinter import *   ## notice lowercase 't' in tkinter here

"""top = Tk()
top.geometry("800x600")
top.title("Inteligentny dźwig")
app=Frame(top)
app.grid()
button=Button(app, text = "Submit")
button.place(relx=0.4, rely=0.95, anchor=CENTER)
button.grid()
# Code to add widgets will go here...
top.mainloop()"""

root = Tk()
root.geometry('800x600')

but_frame = Frame(root)
Button(but_frame, text='SUBMIT', command=None).pack(side=LEFT)
#Button(but_frame, text='Exit', command=root.quit, bg='red', fg='white').pack(side=LEFT)

#but_frame.pack(side=BOTTOM)
but_frame.place(x = 400, y = 300)

root.mainloop()