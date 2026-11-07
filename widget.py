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
