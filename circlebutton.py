import tkinter as tk
from .widget import Widget
class CircleButton(Widget):
    def __init__(self,root,width=50,border_width=1,border_color='#ffffff',
                 text='',fg='#ffffff',bg='#0078d4',command=lambda:None,font=('Arial',10),
                 hover_color='#3395ff',
                 **kwargs):
        super().__init__(root,bg=root.cget('bg'))
        self.text=text
        self.fg=fg
        self.bg=bg
        self.command=command
        self.width=width
        self.font=font
        self.border_width=border_width
        self.border_color=border_color
        self.hover_color=hover_color
        self.canvas=tk.Canvas(self.root,bg=self.root.cget('bg'),height=self.width,
                              highlightthickness=0,width=self.width,**kwargs)
        points=[
            width/2,0,    0.85355*width,0.14645*width,    width,width/2,
            0.85355*width,0.85355*width,    width/2,width,
            0.14645*width,0.85355*width,    0,width/2,    
            0.14645*width,0.14645*width,    width/2,0  
        ]
        self.rect_id=self.canvas.create_polygon(points,smooth=True,splinesteps=1200,
                                      width=self.border_width,fill=self.bg,outline=self.border_color)
        self.text_id=self.canvas.create_text(self.width/2,self.width/2,text=
                                self.text,font=self.font,fill=self.fg)
        self.canvas.bind('<ButtonRelease-1>',lambda events:self.command())
        self.canvas.bind('<Enter>',lambda event:self.canvas.itemconfig(self.rect_id,fill=self.hover_color))
        self.canvas.bind('<Leave>',lambda event:self.canvas.itemconfig(self.rect_id,fill=self.bg))
    def config(self, **kwargs):
        for key, value in kwargs.items():
            if key == 'text':
                self.text = value
                self.canvas.itemconfig(self.text_id, text=value)
            elif key=='width':
                self.width = int(value)       
                self.canvas.config(width=self.width, height=self.width)             
                w = self.width
                points = [
                                w/2, 0,                 0.85355*w, 0.14645*w,    w, w/2,
                                0.85355*w, 0.85355*w,   w/2, w,
                                0.14645*w, 0.85355*w,   0, w/2,    
                                0.14645*w, 0.14645*w,   w/2, 0  
                            ]
                self.canvas.coords(self.rect_id, *points)
                self.canvas.coords(self.text_id, w/2, w/2)
            elif key == 'fg':
                self.fg = value
                self.canvas.itemconfig(self.text_id, fill=value)
            elif key == 'bg':
                self.bg = value
                self.canvas.itemconfig(self.rect_id, fill=value)
            elif key == 'hover_color':
                self.hover_color = value
            elif key == 'font':
                self.font = value
                self.canvas.itemconfig(self.text_id, font=value)
            elif key == 'border_color':
                self.border_color = value
                self.canvas.itemconfig(self.rect_id, outline=value)
            elif key == 'border_width':
                self.border_width = value
                self.canvas.itemconfig(self.rect_id, width=value)
    def cget(self, key):
            if key == "text":
                return self.text
            elif key == "fg":
                return self.fg
            elif key == "bg":
                return self.bg
            elif key == "hover_color":
                return self.hover_color
            elif key == "width":
                return self.width
            elif key == "border_color":
                return self.border_color
            elif key == "border_width":
                return self.border_width
            elif key == "font":
                return self.font
            else:
                raise tk.TclError(f"unknown option \"{key}\"")
    def bind(self,events,command):
        bind_id=self.canvas.bind(events,lambda event,cmd=command:cmd())
        return bind_id
    def unbind(self,events,command=None):
        self.canvas.unbind(events,command)
    def pack(self,*args, **kwargs):
        self.canvas.pack(*args,**kwargs)
    def place(self,*args, **kwargs):
        self.canvas.place(*args,**kwargs)
    def grid(self,*args, **kwargs):
        self.canvas.grid(*args,**kwargs)
