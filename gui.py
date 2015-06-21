from Tkinter import *
import tkFileDialog
from genderflipper import flip, flip_file

class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")   
         
        self.parent = parent
        
        self.initUI()
        self.centerWindow()

    def centerWindow(self):
      
        w = 700
        h = 600

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        
        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
    def initUI(self):

        self.parent.title("The Gender Swapper")
        self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=lambda: self.onOpen(output_text))
        menubar.add_cascade(label="File", menu=fileMenu)

        frame = Frame(width=200, height=200, bg="", colormap="new")
        frame2 = Frame(width=200, height=200, bg="", colormap="new")

        input_text = Text(frame, height=20, width=50, background="#e0e0e0")
        input_text.tag_config("a", foreground="blue", underline=1)
        input_text.insert(INSERT, "Type the original text here...", "a")

        output_text = Text(frame2, height=35, width=50, background="#e0e0e0")
        output_text.tag_config("b", foreground="blue", underline=1)
        output_text.tag_config("c", foreground="blue")
        output_text.insert(INSERT, "and the gender swapped version will appear here!", "b")

        names_text = Text(frame, height=15, width=50, background="#e0e0e0")
        names_text.tag_config("d", foreground="blue", underline=1)
        names_text.insert(INSERT, 'Enter a space separated list of names here (for example " Mary James Ged Serret ").\n Please delete text if no name swaps are required!', "d")

        swapMenu = Menu(menubar)
        swapMenu.add_command(label="Swap Genders", command=lambda: self.swapText(input_text, output_text, names_text))
        menubar.add_cascade(label="Actions", menu=swapMenu)

        swapButton = Button(self, text="Swap Genders", command=lambda: self.swapText(input_text, output_text, names_text))

        swapButton.pack(pady=12)
        input_text.pack(side=TOP)
        names_text.pack(side=TOP)
        frame.pack(side=LEFT)
        output_text.pack()
        frame2.pack(side=RIGHT)
        
    def onOpen(self, output_text):
        ftypes = [('Text files', '*.txt'), ('All files', '*')]
        dlg = tkFileDialog.Open(self, filetypes = ftypes)
        fl = dlg.show()
        
        if fl != '':
            names = {}      
            output_text.delete(1.0, END)        
            output_text.insert(INSERT, flip_file(fl, names), "c")

    def swapText(self, input_text, output_text, name_text):
        names = {}                      
        nameList = name_text.get('1.0', END).split()
        for i in range(len(nameList)/2):
            names[nameList[2*i].lower()] = nameList[2*i+1].lower()

        text = flip(input_text.get('1.0', END), names)
        output_text.delete(1.0, END)
        output_text.insert(INSERT, text, "c")
        
def main():
  
    root = Tk()
    root.geometry("250x120+300+300")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  
