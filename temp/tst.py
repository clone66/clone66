import tkinter as tk
from random import randint
W=150
H=150
root=tk.Tk()
root.geometry(str(W)+'x'+str(H))
root.maxsize(width=150,height=150)

def pos(event):
    #global bl
    x,y=3,5
    canvas.move(bl,x,y)

    print(event.x)

def move_c():
    global x,y,dx,dy
    global bl
    
    x+=dx
    y+=dy
    if x>W or x<=0:
        dx=-dx
      #  dy=-dy
        print('x '+str(x))
        print('dx '+str(dx))

    if y>H or y<=0:
        dy=-dy  
        print('y '+str(y))
        print('dy '+str(dy))
    canvas.move(bl,dx,dy)
    
    root.after(200,move_c)
    




canvas=tk.Canvas(root,width=140,height=140,bg='green')
canvas.pack()



#print(root.winfo_reqwidth())
dx,dy=+15,+13
x,y=15,50

bl=canvas.create_oval(x,y,25,30,fill='red')

move_c()

#print(root.bind('<Button-1>',pos))


#canvas.bind('<Button-1>',move_c)




root.mainloop()