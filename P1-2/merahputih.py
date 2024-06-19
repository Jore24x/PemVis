import numpy as np
import matplotlib.pyplot as plt

#PROGRAM UNTUK TITIK DAN GARIS
print("\033c")       #To close all

row, col = int(500), int(500)
y2, x2 = 250, 450
y1, x1 = 150, 450
y3, x3 = 250, 450
y4, x4 = 350, 450
y5, x5 = 150, 50
y6, x6 = 150, 450
y7, x7 = 150, 50
y8, x8 = 400, 50
pd = int(5)
point_color = [225,0,0]
point_color2 = [255,255,255]
lw = int(5)
line_color = [225,0,0]
line_color2 = [255,255,255]

def buat_garis(Gambar, y1, x1, y2, x2, pd, lw, point_color, line_color):
    pr, pg, pb = point_color
    lr, lg, lb = line_color
    hd = int(pd/2)                               #Calculate the half point diameter.
    hw = int(lw/2)                              #Calculate the half half line width.
    dy = y2-y1
    dx = x2-x1

    # Draw the first point.
    for i in range(x1 - hd, x1 + hd):
        for j in range(y1 - hd, y1 + hd):
            if ((i - x1) * 2 + (j - y1) * 2) < hd ** 2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pg
                Gambar[j, i, 2] = pb

    # Draw the second point.
    for i in range(x2 - hd, x2 + hd):
        for j in range(y2 - hd, y2 + hd):
            if ((i - x2) * 2 + (j - y2) * 2) < hd ** 2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pg
                Gambar[j, i, 2] = pb

    #Draw the line. Untuk garis yang cenderung horisontal
    if abs(dy) <= abs(dx):
        my = dy / dx
        if x2 < x1:        #If x2 < x1 exchange the value of y1 & y2 and x1 & x2.
            temp = y1
            y1 = y2
            y2 = temp
            temp = x1
            x1 = x2
            x2 = temp
        for i in range(x1, x2):
            j = int(my * (i-x1) + y1)           #Finding y using the line equation
            x = i
            y = j
            print('x, y =', x, ',', y)
            for i in range(x-hw, x+hw):        #Creating a circle surrounding (x,y) and coloring it red
                for j in range(y-hw, y+hw):
                    if ( (i-x)*2 + (j-y)*2 ) < hw **2:
                        Gambar[j, i, 0] = lr
                        Gambar[j, i, 1] = lg
                        Gambar[j, i, 2] = lb
    #Draw the line. Untuk garis yang cenderung vertikal
    if abs(dy) > abs(dx):
        mx = dx / dy
        if y2 < y1:        #If y2 < y1 exchange the value of y1 & y2 and x1 & x2.
            temp = y1
            y1 = y2
            y2 = temp
            temp = x1
            x1 = x2
            x2 = temp

        for j in range(y1, y2):
            i = int(mx * (j-y1) + x1)           #Finding y using the line equation
            x = i
            y = j
            print('x, y =', x, ',', y)
            for i in range(x-hw, x+hw):        #Creating a circle surrounding (x,y) and coloring it red
                for j in range(y-hw, y+hw):
                    if ( (i-x)*2 + (j-y)*2 ) < hw **2:
                        Gambar[j, i, 0] = lr
                        Gambar[j, i, 1] = lg
                        Gambar[j, i, 2] = lb

    return Gambar

print('col, row =', col, ',', row)
Gambar = np.zeros(shape=(row, col, 3), dtype=np.uint8)  # Preparing the black canvas


while x2 > 50 and x1 > 50 :
    hasil = buat_garis(Gambar, y1, x1, y2, x2, pd, lw, point_color, line_color)
    Gambar = hasil
    x2 -= 1
    x1 -= 1
while x4 > 50 and x3 > 50 :
    hasil = buat_garis(Gambar, y3, x3, y4, x4, pd, lw, point_color2, line_color2)
    Gambar = hasil
    x4 -= 1
    x3 -= 1
# hasil = buat_garis(Gambar, y3, x3, y4, x4, pd, lw, point_color, line_color)
# Gambar = hasil
# hasil = buat_garis(Gambar, y5, x5, y6, x6, pd, lw, point_color, line_color)
# Gambar = hasil
# hasil = buat_garis(Gambar, y7, x7, y8, x8, pd, lw, point_color, line_color)
# Gambar = hasil

plt.figure('Rotasi')
plt.imshow(hasil)
plt.show()