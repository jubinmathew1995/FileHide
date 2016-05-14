__author__ = 'Jubin & Raghava'
import Tkinter as tk
import os
import tkFileDialog as fd
import zipper
import tkMessageBox
import ttk

Top = tk.Tk()
Top.title("FileHide")
logo = tk.PhotoImage(file="ic_launcher.gif")
Top.tk.call('wm', 'iconphoto', Top._w, logo)
src = tk.StringVar()
dst = tk.StringVar()
Top.minsize(250, 300)
Top.maxsize(250, 300)
defaultFrame = ttk.Frame(Top)


def updateLV():
    i = 0
    listview.delete(0, tk.END)
    for (dirpath, dirnames, filenames) in os.walk(os.getcwd() + "/output"):
        for f in filenames:
            listview.insert(i, f)
            i += 1


def onZip(*functions):
    if (os.path.isfile(src.get()) and os.path.isfile(dst.get())):
        functions[0]()
        zipper.zipFun(src.get(), dst.get())
        src.set("")
        dst.set("")
        tkMessageBox.showinfo("Completed", "Mask was successful")
        updateLV()
    else:
        tkMessageBox.showerror("Error", "Invalid files")


def onUnzip(*functions):
    if (os.path.isfile(src.get())):
        functions[0]()
        zipper.unzipFun(src.get())
        tkMessageBox.showinfo("Completed", "Unmask was successful")
        updateLV()


def Browse(pt, dir):
    result = fd.askopenfilename(parent=pt, initialdir=os.getcwd(), title="Browse")
    globalv = globals()
    globalv[dir].set(result)


def maskFun():
    newTop = tk.Toplevel(Top)
    newTop.minsize(200, 150)
    newTop.maxsize(200, 150)
    logo = tk.PhotoImage(file="ic_launcher.gif")
    newTop.tk.call('wm', 'iconphoto', newTop._w, logo)
    maskFrame = ttk.Frame(newTop)
    File2hide = ttk.LabelFrame(maskFrame, text="Files To Hide", )
    EntryField1 = ttk.Entry(File2hide, textvariable=src)
    Browse1 = ttk.Button(File2hide, text="Browse", command=lambda: Browse(newTop, "src"))
    File2hideIn = ttk.LabelFrame(maskFrame, text="Files To Hide In", )
    EntryField2 = ttk.Entry(File2hideIn, textvariable=dst)
    Browse2 = ttk.Button(File2hideIn, text="Browse", command=lambda: Browse(newTop, "dst"))
    OkButton = ttk.Button(maskFrame, text="Mask", command=lambda: onZip(newTop.destroy))
    EntryField1.pack(side=tk.LEFT)
    Browse1.pack(side=tk.LEFT)
    File2hide.pack()
    EntryField2.pack(side=tk.LEFT)
    Browse2.pack(side=tk.LEFT)
    File2hideIn.pack()
    OkButton.pack(side=tk.RIGHT)
    maskFrame.pack()
    newTop.mainloop()


def unmaskFun():
    newTop = tk.Toplevel(Top)
    newTop.minsize(200, 150)
    newTop.maxsize(200, 150)
    logo = tk.PhotoImage(file="ic_launcher.gif")
    newTop.tk.call('wm', 'iconphoto', newTop._w, logo)
    unmaskFrame = ttk.Frame(newTop)
    File2hide = ttk.LabelFrame(unmaskFrame, text="Files To Hide", )
    EntryField1 = ttk.Entry(File2hide, textvariable=src)
    Browse1 = ttk.Button(File2hide, text="Browse", command=lambda: Browse(newTop, "src"))
    OkButton = ttk.Button(unmaskFrame, text="Unmask", command=lambda: onUnzip(newTop.destroy))
    EntryField1.pack(side=tk.LEFT)
    Browse1.pack(side=tk.LEFT)
    File2hide.pack()
    OkButton.pack(side=tk.RIGHT)
    unmaskFrame.pack()
    newTop.mainloop()


mask = ttk.Button(defaultFrame, text="Mask", command=maskFun)
unmask = ttk.Button(defaultFrame, text="Unmask", command=unmaskFun)
menubar = tk.Menu(Top, relief=tk.FLAT)
filemenu = tk.Menu(menubar, tearoff=0, relief=tk.FLAT)
helpmenu = tk.Menu(menubar, tearoff=0, relief=tk.FLAT)
filemenu.add_command(label="Mask", command=maskFun)
filemenu.add_command(label="Unmask", command=unmaskFun)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=Top.destroy)
helpmenu.add_command(label="About")
menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Help", menu=helpmenu)
Top.config(menu=menubar)
listitems = tk.StringVar()
Output = ttk.Labelframe(defaultFrame, text="Output directory")
listview = tk.Listbox(Output, listvariable=listitems, width=250, height=200)


def onselect(evt):
    wd = evt.widget
    index = int(wd.curselection()[0])
    value = wd.get(index)
    os.startfile(os.getcwd() + "/output/" + value, 'open')
    listview.select_clear(0, tk.END)
    Top.update()
    print os.getcwd() + "/output/" + value


updateLV()
listview.bind('<<ListboxSelect>>', onselect)
mask.pack()
unmask.pack()
listview.pack(fill="both", expand=True)
Output.pack(side="left", fill="both", expand=True)
defaultFrame.pack()
defaultFrame.tkraise()
Top.mainloop()
