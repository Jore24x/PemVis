from tkinter import *
from tkinter.ttk import *

from plotdata import regression_plot
from stats import stats_columns


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.winfo_toplevel().title('dataview')
        self.l1 = Label(self.master, text="File Name")
        self.l2 = Label(self.master, text="X Label")
        self.l3 = Label(self.master, text="Y Label")

        self.l1.grid(row=0, sticky=W)
        self.l2.grid(row=1, sticky=W)
        self.l3.grid(row=2, sticky=W)

        self.eFname = Entry(self.master, width=40)
        self.eXname = Entry(self.master, width=40)
        self.eYname = Entry(self.master, width=40)

        self.eFname.grid(row=0, column=1)
        self.eXname.grid(row=1, column=1)
        self.eYname.grid(row=2, column=1)

        self.txtX = Text(self.master, width=30, height=10)  # Added height to the Text widgets
        self.txtY = Text(self.master, width=30, height=10)

        self.txtX.grid(row=3, column=0, sticky=W)
        self.txtY.grid(row=3, column=1, sticky=W)

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.style = Style()
        self.style.map('D.TButton', foreground=[('pressed', 'red'), ('active', 'green')],
                       background=[('pressed', 'black'), ('active', 'white')])

        self.btn_graph = Button(self.master, text="Show Regression Graph", style="D.TButton", command=self.show_graph)
        self.btn_graph.grid(row=4, column=0, sticky=W)

        self.btn_stats = Button(self.master, text="Show Stats", style="D.TButton", command=self.show_stats)
        self.btn_stats.grid(row=4, column=1, sticky=W)

        self.quit = Button(self.master, text="Quit", style="D.TButton", command=self.master.destroy)
        self.quit.grid(row=4, column=2, sticky=E)  # Changed column to 2 to avoid overlap

    def show_graph(self):
        regression_plot(self.eFname.get(), self.eXname.get(), self.eYname.get())

    def show_stats(self):
        xstats, ystats = stats_columns(self.eFname.get(), self.eXname.get(), self.eYname.get())
        self.txtX.delete('1.0', END)  # Clear the Text widget before inserting new text
        self.txtY.delete('1.0', END)
        self.txtX.insert(INSERT, xstats)
        self.txtY.insert(INSERT, ystats)


root = Tk()
app = Application(master=root)
app.mainloop()