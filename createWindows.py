import tkinter

#define window
root = tkinter.Tk()

root.title('Window basics')  # set title

# set icon of window
# root.iconbitmap('filename.jpg')

root.geometry('400x400')  # size of window

root.resizable(0,0)  # if you don't want your window to resize

root.config(bg='blue')  # set bg color


# another window
root1 = tkinter.Toplevel()
root1.title('another window')
root1.config(bg='red')

root1.geometry('200x200+500+50')  #+500+50 means at horizontal 500 unit and vertical 50 unit window will be set

# run root window's main loop
root.mainloop()