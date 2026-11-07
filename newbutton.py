import tkinter as tk
from .widget import Widget
class NewButton(Widget):
    def __init__(self,root,text='',fg='#ffffff',bg="#0078d4",
                 width=80,height=40,radius=6,command=lambda:None
                 ,hover_color='#3395FF',font=('Arial',10),border_width=0,
                 border_color=None,
                 **kwargs):
        super().__init__(root,bg)
        self.border_width=border_width
        self.border_color=border_color
        self.text=text
        self.hover_color=hover_color
        self.command=command
        self.width=int(width)
        self.font=font
        self.fg=fg
        self.bg=bg
        self.height=int(height)        
        self.radius=radius
        self.canvas=tk.Canvas(self.root,width=self.width,height=self.height,
                              highlightthickness=0,bg=self.root.cget('bg'),**kwargs)
        if self.radius == 'normal' or self.radius >= self.height / 2:
            r = self.height / 2
        else:
            r = int(self.radius)
        mid_width=self.width/2
        points = [
            r, 0,               mid_width, 0,       self.width - r, 0,
            self.width, 0,      self.width, r,      
            self.width, self.height - r,            
            self.width, self.height,                
            self.width - r, self.height, mid_width, self.height, r, self.height,
            0, self.height,     0, self.height - r, 
            0, r,                                   
            0, 0,               r, 0                
        ]
        self.rect_id=self.canvas.create_polygon(points,smooth=True,fill=self.bg,splinesteps=1200,
                                      outline=self.border_color,width=self.border_width)
        self.text_id=self.canvas.create_text(mid_width,self.height/2,text=self.text,width=self.width-20,
                                font=self.font,fill=self.fg)
        self.canvas.bind('<ButtonRelease-1>',lambda event:self.command())
        self.canvas.bind('<Enter>',lambda event:self.canvas.itemconfig(self.rect_id,fill=self.hover_color))
        self.canvas.bind('<Leave>',lambda event:self.canvas.itemconfig(self.rect_id,fill=self.bg))
    def pack(self,*args, **kwargs):
        self.canvas.pack(*args,**kwargs)
    def place(self,*args, **kwargs):
        self.canvas.place(*args,**kwargs)
    def grid(self,*args, **kwargs):
        self.canvas.grid(*args,**kwargs)
    def config(self, **kwargs):
            for key, value in kwargs.items():
                if 'width' in kwargs or 'height' in kwargs or 'radius' in kwargs:
                    if 'width' in kwargs: 
                        self.width = int(kwargs['width'])
                    if 'height' in kwargs: 
                        self.height = int(kwargs['height'])
                    if 'radius' in kwargs: 
                        self.radius = kwargs['radius']
                    self.canvas.config(width=self.width, height=self.width)
                    if self.radius == 'pill' or self.radius >= self.height / 2:
                        r = self.height / 2
                    else:
                        r = int(self.radius)
                        mid_width=self.width/2
                    points = [
                                r, 0,               mid_width, 0,       self.width - r, 0,
                                self.width, 0,      self.width, r,      
                                self.width, self.height - r,            
                                self.width, self.height,                
                                self.width - r, self.height, mid_width, self.height, r, self.height,
                                0, self.height,     0, self.height - r, 
                                0, r,                                   
                                0, 0,               r, 0                
                            ]
                    self.canvas.coords(self.rect_id, *points)
                    self.canvas.coords(self.text_id, mid_width, self.height/2)
                
                elif key == 'text':
                    self.text = value
                    self.canvas.itemconfig(self.text_id, text=value)
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
                    self.border = value
                    self.canvas.itemconfig(self.rect_id,width=value) 
                elif key == 'command':
                    self.command = value
                    self.canvas.itemconfig(self.rect_id,command=value)
    def bind(self,events,command):
        bind_id=self.canvas.bind(events,lambda event,cmd=command:cmd())
        return bind_id
    def unbind(self,events,command=None):
        self.canvas.unbind(events,command)
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
                elif key == 'height':
                    return self.height
                elif key == 'radius':
                    return self.radius
                elif key == "border_color":
                    return self.border_color
                elif key == "border_width":
                    return self.border_width
                elif key == "font":
                    return self.font
                else:
                    raise tk.TclError(f"unknown option \"{key}\"")
