
import tkinter as tk
from pyfiglet import Figlet


class MyGUI():

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('ASCILL converter')
        # self.root.geometry('800x400')

        


        self.entbtnfr = tk.Frame(self.root)

        self.ent = tk.Entry(self.entbtnfr,font=('Arial',18))
        self.ent.pack(padx=10,fill='x',side='left')

        self.ent.bind('<KeyPress>',self.shortcut)
        self.btn = tk.Button(self.entbtnfr,text='Convert',font=('Arial',18),command=self.convert)
        self.btn.pack(side='left')


        self.entbtnfr.pack(padx=10,pady=10)

        self.textbox = tk.Text(self.root,)
        self.textbox.pack(padx=10,pady=10)




        self.root.mainloop()
    def shortcut(self,event):
        if event.keysym == 'Return':
            self.convert()

    def convert(self):
        f = Figlet(font='doom')
        self.textbox.delete('1.0',tk.END)
        # print(f.renderText(self.ent.get()))
        self.textbox.insert('1.0',f.renderText(self.ent.get()))



MyGUI()