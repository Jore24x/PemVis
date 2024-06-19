import tkinter as tk



root= tk.Tk()

Frameku= tk.Frame(root, bg= 'blue')
Frameku.place(relwidth = 1, relheight= 1)

Tombolku = tk.Button(Frameku, text= "Tes Tombol", bg='gray', fg = 'red')
Tombolku.pack()

Entryku = tk.Entry(Frameku, bg = 'green')
Entryku.pack()

root.mainloop()