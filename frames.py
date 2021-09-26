import tkinter
from tkinter import BOTH
#basic set up
root = tkinter.Tk()
root.title('Demo frames')
root.geometry('400x400')

#define frames
frame = tkinter.Frame(root, bg="blue")
frame1 = tkinter.Frame(root, bg = "red")
frame2 = tkinter.LabelFrame(root , text="this is labled frame" , borderwidth=3)

#pack frames in root
frame.pack(fill=BOTH , expand=True)   #fill both means it will expand in both the direction 
frame1.pack(fill='x' , expand=True)     #fill x means it will expand in X completely and expand the necessary space in Y
frame2.pack(fill=BOTH , expand=True , padx=10 , pady=5)

#put label in frames
tkinter.Label(frame , text="Hello!").pack()
tkinter.Label(frame , text="Hello!").pack()

tkinter.Label(frame1 , text="Hi there").grid(row=0 , column=0)
tkinter.Label(frame1 , text="Hi there").grid(row=1 , column=1)
tkinter.Label(frame1 , text="Hi there").grid(row=5 , column=2)
tkinter.Label(frame1 , text="r4").grid(row=4 , column=3)


#display in loop
root.mainloop()