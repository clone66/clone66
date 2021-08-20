import tkinter as tk
W=150
H=150


class Ball:
    def __init__(self):
        self.dx,self.dy=4,6
        self.x,self.y=15,50
        self.bl=canvas.create_rectangle(11,44,25,30,fill='red')
   
    def move(self):
        self.x+=self.dx
        self.y+=self.dy
        if self.x>W or self.x<=0:
            self.dx=-self.dx
            
            print('x '+str(self.x))
            print('dx '+str(self.dx))

        if self.y>H or self.y<=0:
            self.dy=-self.dy  
            print('y '+str(self.y))
            print('dy '+str(self.dy))
        canvas.move(self.bl,self.dx,self.dy)
    
def tick():
    ball.move()     
    root.after(50,tick)

def main():
    global canvas,root,ball
    root=tk.Tk()
    root.geometry(str(W)+'x'+str(H))
    root.maxsize(width=170,height=170)
    canvas=tk.Canvas(root,width=140,height=140,bg='green')
    canvas.pack()
    ball=Ball()
    tick()
    root.mainloop()

main()



