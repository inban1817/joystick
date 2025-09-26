import pygame as pg
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

pg.init()
pg.init()
js=pg.joystick.Joystick(0)
js.init()


plt.ion()
r=True
while r:
    for event in pg.event.get():
        if js.get_button(0):
            r=False
    x=js.get_axis(0)
    y=-js.get_axis(1) 
    print(js.get_axis(0),js.get_axis(1))


    plt.clf()
    plt.scatter(x,y)
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.title('joystick Position as Joystick Axes')
    plt.grid(True)
    plt.pause(0.01)
        

        
pg.quit()