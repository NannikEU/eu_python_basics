from tkinter import *
import tkinter as tk
import threading
import math
from datetime import datetime

now = datetime.now()
time = now.hour * 60 + now.minute
speedScale = 1
windowSize = {
    'x': 500,
    'y': 500
}
clockCenterPoint = {
    'x': windowSize['x'] / 2,
    'y': windowSize['y'] / 2
}


class App(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.quit()

    # create window and canvas
    def run(self):
        self.root = tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        self.root.geometry("{}x{}".format(windowSize['x'], windowSize['y']))

        self.canvas = tk.Canvas(self.root, width=windowSize['x'], height=windowSize['y'], bg='#ccc')
        self.canvas.pack()

        self.speedScaleInput = StringVar()

        message_entry = Entry(textvariable = self.speedScaleInput)
        message_entry.place(anchor = "c", width = 120, height = 20, x = 70, y = 15)

        message_button = Button(text = "Submit", command = self.updateSpeed)
        message_button.place(anchor = "c", width = 120, height = 20, x = 70, y = 45)

        self.update()
        self.root.mainloop()

    def updateSpeed(self):
        global speedScale
        if self.speedScaleInput.get().isnumeric():
            speedScale = int(self.speedScaleInput.get())

    # clock loop
    def update(self):
        global time
        self.draw()
        time = (time + 1) % (60 * 12)

        self.root.after(int(1000 / speedScale), self.update)

    # draw clock each frame
    def draw(self):
        global time
        self.canvas.delete('all')

        dashIntend = 120
        dashSize = 5
        minuteLineSize = 100
        hourLineSize = 70

        radCoef = 2 * math.pi / 60

        # minute
        self.canvas.create_line(clockCenterPoint['x'],
                                clockCenterPoint['y'],
                                clockCenterPoint['x'] + math.sin(time * radCoef) * minuteLineSize,
                                clockCenterPoint['y'] + -math.cos(time * radCoef) * minuteLineSize)

        # hour
        self.canvas.create_line(clockCenterPoint['x'],
                                clockCenterPoint['y'],
                                clockCenterPoint['x'] + math.sin(math.floor(time / 60) * 5 * radCoef) * hourLineSize,
                                clockCenterPoint['y'] + -math.cos(math.floor(time / 60) * 5 * radCoef) * hourLineSize)

        # dashs
        for i in range(60):
            s = dashSize * 2.5 if i % 5 == 0 else dashSize
            self.canvas.create_line(clockCenterPoint['x'] + math.sin(i * radCoef) * dashIntend,
                                    clockCenterPoint['y'] + -math.cos(i * radCoef) * dashIntend,
                                    clockCenterPoint['x'] + math.sin(i * radCoef) * dashIntend - math.sin(i * radCoef) * s,
                                    clockCenterPoint['y'] + -math.cos(i * radCoef) * dashIntend - -math.cos(i * radCoef) * s)


app = App()
