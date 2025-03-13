import tkinter as tk
import time

WIDTH, HEIGHT = 800, 600
X_OFFSET, Y_OFFSET = WIDTH // 2, HEIGHT // 2
SCALE = 40

def transform(x, y):
    return X_OFFSET + x * SCALE, Y_OFFSET - y * SCALE

root = tk.Tk()
root.title("Le Jeu des cercles")

frame1 = tk.Frame(root)
frame1.pack(side = "left")

frame2 = tk.Frame(root)
frame2.pack(side="right")
canvas1 = tk.Canvas(frame1, width=WIDTH, height=HEIGHT, bg="white")
canvas1.pack()
canvas2 = tk.Canvas(frame2, width=WIDTH, height=HEIGHT, bg="white")
canvas2.pack()
#x0, y0 = transform(4 - 4, 0 + 4)
#x1, y1 = transform(4 + 4, 0 - 4)
#canvas.create_oval(x0, y0, x1, y1, outline="red", width=2)

couleurs = [None, None, "white", "red", "blue"]
x0, y0 = transform(-2.4 - 5.6, 0 + 5.6)
x1, y1 = transform(-2.4 + 5.6, 0 - 5.6)
coords_set = {
        "c0": [[transform(-5.95 - 8.67, 0 + 8.67), transform(-5.95 + 8.67, 0 - 8.67), 23.51, -47.02], [transform(4 - 4, 0 + 4), transform(4 + 4, 0 - 4), 120.03, 119.94],2],
        "c1": [[transform(-2.4 - 8.4, -10.62 + 8.4), transform(-2.4 + 8.4, -10.62 - 8.4), 58.41, 63.18],[(x0, y0), (x1, y1),-38.17,-103.66],3],
        "c2": [[transform(-10.22 - 4.87, 0 + 4.87), transform(-10.22 + 4.87, 0 - 4.87), 45.33, -90.65],[(x0,y0), (x1, y1), 141.83, 76.34], 3],
        "c3": [[transform(-2.4 - 8.4, 10.62 + 8.4), transform(-2.4 + 8.4, 10.62 - 8.4), -58.41, -63.18],[(x0,y0), (x1,y1),38.17, 103.66], 3],
        "c4": [[transform(9.01 - 8.71, 8.66 + 8.71), transform(9.01 + 8.71, 8.66 - 8.71), -96.65, -46.78],[transform(4 - 4, 0 + 4), transform(4 + 4, 0 - 4), 0, 120.03],4],
        "c5": [[transform(9.01 - 8.71, -8.66 + 8.71), transform(9.01 + 8.71, -8.66 - 8.71), 96.65, 46.78],[transform(4 - 4, 0 + 4), transform(4 + 4, 0 - 4), 0, -120.03],4]
        }
traced1 = {}
traced2 = {}
for nom, info in coords_set.items():
    traced1[nom] = [
            canvas1.create_arc(info[0][0][0], info[0][0][1],
                              info[0][1][0], info[0][1][1],
                              outline=couleurs[info[2]], fill=couleurs[info[2]],
                              style='chord',
                              start=info[0][2],extent = info[0][3]),

            canvas1.create_arc(info[1][0][0], info[1][0][1],
                              info[1][1][0], info[1][1][1],
                              outline=couleurs[info[2]], fill=couleurs[info[2]],
                              style='chord', 
                              start=info[1][2],extent = info[1][3])
            ]
    traced2[nom] = [
            canvas2.create_arc(info[0][0][0], info[0][0][1],
                              info[0][1][0], info[0][1][1],
                              outline=couleurs[info[2]], fill=couleurs[info[2]],
                              style='chord',
                              start=info[0][2],extent = info[0][3]),

            canvas2.create_arc(info[1][0][0], info[1][0][1],
                              info[1][1][0], info[1][1][1],
                              outline=couleurs[info[2]], fill=couleurs[info[2]],
                              style='chord', 
                              start=info[1][2],extent = info[1][3])

        ]
    canvas1.create_arc(info[0][0][0], info[0][0][1],
                      info[0][1][0], info[0][1][1],
                      outline='black', style='arc',
                      width=3,
                      start=info[0][2],extent = info[0][3])

    canvas1.create_arc(info[1][0][0], info[1][0][1],
                      info[1][1][0], info[1][1][1],
                      outline='black', style='arc',
                      width=3,
                      start=info[1][2],extent = info[1][3])
    canvas2.create_arc(info[0][0][0], info[0][0][1],
                      info[0][1][0], info[0][1][1],
                      outline='black', style='arc',
                      width=3,
                      start=info[0][2],extent = info[0][3])

    canvas2.create_arc(info[1][0][0], info[1][0][1],
                      info[1][1][0], info[1][1][1],
                      outline='black', style='arc',
                      width=3,
                      start=info[1][2],extent = info[1][3])



#x0, y0 = transform(4 - 4, 0 + 4)
#x1, y1 = transform(4 + 4, 0 - 4)
#canvas.create_oval(x0, y0, x1, y1, outline="red", width=2)
print(traced2)
def change1(pos):
    i = 0
    for nom, obj in traced1.items():
        canvas1.itemconfig(obj[0], fill=couleurs[pos[i]], outline=couleurs[pos[i]])
        canvas1.itemconfig(obj[1], fill=couleurs[pos[i]], outline=couleurs[pos[i]])
        i+=1
    root.update()


def change2(pos):
    i = 0
    for nom, obj in traced2.items():
        canvas2.itemconfig(obj[0], fill=couleurs[pos[i]], outline=couleurs[pos[i]])
        canvas2.itemconfig(obj[1], fill=couleurs[pos[i]], outline=couleurs[pos[i]])
        i+=1
    root.update()

#while True:
#    position = change1([3,2,3,3,4,4])
#    time.sleep(0.5)
#    position = change1([3,3,2,3,4,4])
#    time.sleep(0.5)
#    position = change1([4,3,2,3,3,4])
#    time.sleep(0.5)
#    position = change1([4,3,2,3,4,3])
#    time.sleep(0.5)
#    change1([3,4,3,2,4,3])
#    time.sleep(0.5)
#    change1([2,3,4,3,4,3])
#    time.sleep(0.5)
#    change1([3,2,3,4,4,3])
#    time.sleep(0.5)
#    change1([4,3,2,3,4,3])
#    time.sleep(0.5)
#    change1([3,3,2,3,4,4])
#    time.sleep(0.5)
#    change1([3,3,3,2,4,4])
#    time.sleep(0.5)
#    change1([2,3,3,3,4,4])
#    time.sleep(0.5)

root.mainloop()
