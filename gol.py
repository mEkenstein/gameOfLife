#!/usr/bin/python

import os
import time
from tkinter import *
import threading
import math

class Point:
    def __init__(self, ix):
        pass


class Board:

    _activePos = set()
    _potentialPos = set()
    _frameRate = 2
    _tFrame = _frameRate / 2
    _running = 0

    def __init__(self, b, size):
        self._activePos = b
        self._size = size
        self._frames = []
        self._defBoard = b.copy()
        self._points = []

    def ResetBoard(self):
        if self._running:
            self._running = 0
        if (self._activePos):
            for p in self._activePos:
                if self.point2ix(p) in range(0, self._size * self._size):
                    self._frames[self.point2ix(p)].configure(bg="white")
            self._activePos.clear()
        self._activePos = self._defBoard.copy()
        self.printBoard()

    def addFrame(self, frame):
        self._frames.append(frame)

    def lClick(self, event):
        frame = event.widget
        ix = self._frames.index(frame)
        p = self.ix2point(ix)
        print("ix ", ix)
        print("point ", p)
        if p in self._activePos:
            frame.configure(bg="white")
            self._activePos.remove(p)
        else:
            frame.configure(bg="yellow")
            self._activePos.add(p)

    #This is probably broken
    def point2ix(self, point):
        x, y = point
        x = x + self._size / 2 - 1
        y = y + self._size / 2
        ix = x + y * self._size + 1
        return int(ix)

    def ix2point(self, ix):
        y = int(math.floor(ix / self._size) - self._size / 2)
        x = int(ix % self._size - self._size / 2)
        return (x,y)

    def Neighbours(self, point):
        x, y = point
        yield (x-1, y-1)
        yield (x, y-1)
        yield (x+1, y-1)
        yield (x-1, y)
        yield (x+1, y)
        yield (x-1, y+1)
        yield (x, y+1)
        yield (x+1, y+1)

    def NewEmptyBoard(self):
        newBoard = set()
        for l in self._activePos:
            neighbourGen = self.Neighbours(l)
            for p in neighbourGen:
                newBoard.add(p)
        self._potentialPos = newBoard

    def evolve(self):
        nextBoard = set()
        self.NewEmptyBoard()
        for p in self._potentialPos:
            nActive = 0
            neighbourGen = self.Neighbours(p)
            for op in neighbourGen:
                if (op in self._activePos):
                    nActive = nActive + 1
            # print(p," has " , nActive," n of neighbors")
            if (nActive == 3 or (nActive == 2 and (p in self._activePos))):
                nextBoard.add(p)
        self._activePos = nextBoard

    def printBoard(self):
        for i in range(len(self._frames)):
            p = self.ix2point(i)
            if p in self._activePos:
                self._frames[i].configure(bg="yellow")
            else:
                self._frames[i].configure(bg="white")
                if p in self._activePos:
                    self._activePos.remove(p)

    def RunEvolution(self):
        while(self._running):
            self.evolve()
            self.printBoard()
            time.sleep(self._tFrame)
        print("Done")

    def Start(self, frames):
        #frames[1].configure(bg="yellow")
        if (not self._running):
            self._running = 1
            to = threading.Thread(target=self.RunEvolution, args=(), daemon=True)
            to.start()
            print("Evolution started")

    def StopEvolution(self):
        self._running = 0

    def GetFrameRate(self):
        return self._frameRate

    def SetFrameRate(self, val):
        self._frameRate = int(val)
        self._tFrame = 1 / self._frameRate

    def GetBoard(self):
        return self._activePos


def main():
    gridSize = 26
    nPixelsPerBtn = 18

    win = Tk()
    win.title("Game of life")
    winSize = str(gridSize * nPixelsPerBtn) + "x" + str(gridSize * nPixelsPerBtn+50)
    win.resizable(False, False)
    win.geometry(winSize)

    Grid.rowconfigure(win, 0, weight=1)
    Grid.columnconfigure(win, 0, weight=1)
    frame = Frame(win, background="gray5")
    frame.grid(sticky=N+E+W)
    frameLower = Frame(win)
    frameLower.grid(sticky=S+W)

    frames = []
    b = Board(set([(0, 0), (-1,0), (1, 0), (0, 1)]), gridSize)

    for y in range(1,gridSize+1):
        pass
        Grid.rowconfigure(frame, y, weight=1)
        for x in range(1,gridSize+1):
            Grid.columnconfigure(frame, x, weight=1)
            fr = Frame(frame, width=nPixelsPerBtn, height=nPixelsPerBtn, bg="white")
            fr.grid(row=y, column=x, padx=1, pady=1)
            fr.bind("<Button-1>", b.lClick)
            b.addFrame(fr)
    b.printBoard()

    btnWidth = 14
    Button(frameLower, text="Start", width=btnWidth, command=lambda: b.Start(frames)).grid(row=0, column=0, sticky=W)
    Button(frameLower, text="Pause", width=btnWidth, command=b.StopEvolution).grid(row=0, column=1, sticky=W)
    Button(frameLower, text="Reset", width=btnWidth, command=b.ResetBoard).grid(row=0, column=2, sticky=W)
    Grid.columnconfigure(frameLower, 4, pad= str(gridSize* nPixelsPerBtn - 3 * btnWidth*10))

    Button(frameLower, text="Exit", width=btnWidth, command=win.quit).grid(row=2, column=4, sticky=E)
    slider = Scale(frameLower, from_=1, to=15, orient=HORIZONTAL, command=b.SetFrameRate, showvalue=0, label="Speed")
    slider.grid(row=2, column=0, sticky=W)
    slider.set(b.GetFrameRate())
    win.mainloop()


main()
