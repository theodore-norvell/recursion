import tkinter as tk
import time

root = tk.Tk()

c = tk.Canvas( root, width=100, height=100 )

r = c.create_rectangle( 20, 20, 80, 80, fill="#ff0000" )

def mkMover( count, item, canv, dx, dy, dt ) :
    def mover() :
        if count > 0 :
            canv.move( item, dx, dy )
            root.after( dt, mkMover(count-1, item, canv, dx, dy, dt) )
    return mover

b = tk.Button( root, text="Go", command = mkMover( 10, r, c, 2, 2, 100 ) )
b.pack()


class Hanoi
    def __init__( self, count, tk, root, w, h )
        self.count = count
        self.w = w 
        self.h = h
        self.tk = tk
        self.root = root
        self.canv = tk.Canvas( root, width=w, height=h )
        self.spindles = [ [], [], [] ] 
        for i in range(0, count) :
            self.spindles[0].append( [i] )
        self.disks = {}
        for i in  range(0, count) :
            self.disks = self.disks.union( new Disk(i, 0, count-i-1, canv ) )



c.pack()
root.mainloop() 
