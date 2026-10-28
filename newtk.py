import tkinter as tk
class Widget():
    def __init__(self,root,bg=None):
        self.root=root
        self.bg=bg
        self.Transparency=0
        self.out=1
    def Fade_in(self):
        self.root.attributes('-alpha',0)
        def use_now():
            if self.Transparency<1.0:
                self.Transparency+=0.01
                self.root.attributes('-alpha',self.Transparency)
                self.root.after(10,use_now)
            elif self.Transparency>=1.0:
                self.Transparency=1.0
                self.root.attributes('-alpha',1)
        use_now()
    def dark(self):
        self.root.config(bg='#1e1e1e')
    def light(self):
        self.root.config(bg='#f5f5f7')
    def set_opacity(self,num):
        self.root.update()
        self.root.attributes('-alpha',num)
    def Fade_out(self):
        def see_now():
            if self.out>=0:
                self.out-=0.1
                self.root.attributes('-alpha',self.out)
                self.root.after(10,see_now)
            else:
                self.out=0
                self.root.attributes('-alpha',0)
                self.root.after(200, self.root.destroy) 
        see_now()
class NewButton(Widget):
    def __init__(self,root,text='',cmd=None,bg=None):
        super().__init__(root,bg=bg)
        self.text=text
        self.cmd=cmd
    def use(self):
        self.widget=tk.Label(self.root,text=self.text,bg=self.bg)
        self.widget.bind('<Button-1>',lambda events:self.cmd())
        return self.widget
    def hover(self,hover_bg='',leave_bg=''):
        self.widget.bind('<Enter>',lambda events,c=self.widget:c.config(bg=hover_bg))
        self.widget.bind('<Leave>',lambda events,c=self.widget:c.config(bg=leave_bg))
class NewEntry(Widget):
    def __init__(self,root,show='',hovertext='',width='',bg=None,size=None):
        super().__init__(root,bg)
        self.size=size
        self.show=show
        self.hovertext=hovertext
        self.width=width
    def use(self):
        self.widget=tk.Entry(self.root,bg=self.bg,relief='flat',bd=0,width=self.width
    ,show='',
    highlightthickness=1, 
    highlightbackground="gray",
    highlightcolor="#0078D7",font=("Arial", self.size))
        self.widget.insert(tk.END,self.hovertext)
        self.widget.config(fg='gray')
        return self.widget
    def hover_text(self):
        self.widget.bind('<FocusIn>',self.Foucus_In)
        self.widget.bind('<FocusOut>',self.Foucus_Out)
    def Foucus_In(self,events):
        if self.widget.get() == self.hovertext:
            self.widget.delete(0, tk.END)
            self.widget.config(fg="black",show=self.show)
    def Foucus_Out(self,events):
        if not self.widget.get():
            self.widget.config(show='')
            self.widget.insert(tk.END,self.hovertext)
            self.widget.config(fg='grey')
    def add(self,text):
        if self.widget.get() == self.hovertext:
            self.widget.delete(0, tk.END)
            self.widget.config(fg='black')
        self.widget.insert(tk.END,text)
    def clear(self,start=0,end=tk.END):
        self.widget.delete(start, end)
        if not self.widget.get() and self.hovertext:
            self.widget.insert(tk.END, self.hovertext)
            self.widget.config(fg='gray')
def main():
    root=tk.Tk()
    root.title('show')
    root.geometry('300x300')
    a1=Widget(root)
    a1.Fade_in()
    a1.dark()
    btn1=NewButton(root,text='hello',cmd=lambda:entry1.clear(0,2),bg='red')
    btn1.use().place(x=0,y=0)
    btn1.hover(leave_bg='red',hover_bg='blue')
    entry1=NewEntry(root,bg='white',size=15,width=20,hovertext='hello')
    entry1.use().pack()
    entry1.hover_text()
    entry1.add('hell')
    root.mainloop()
if __name__=='__main__':
    main()
